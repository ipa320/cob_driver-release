/*
 * Copyright 2017 Fraunhofer Institute for Manufacturing Engineering and Automation (IPA)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0

 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
 
//ROS typedefs
#include "ros/ros.h"
#include <cob_msgs/PowerState.h>
#include <cob_msgs/EmergencyStopState.h>
#include <std_msgs/Float64.h>
#include <algorithm>

class cob_voltage_control_config
{
public:
    double min_voltage;
    double max_voltage;
    double max_voltage_res;
    int num_voltage_port;
    int num_em_stop_port;
    int num_scanner_em_port;
};

class cob_voltage_control_data
{
// autogenerated: don't touch this class
public:
    //configuration data

    //input data
    int in_phidget_voltage;
    int in_phidget_current;

    //output data
    cob_msgs::PowerState out_pub_power_state_;
    cob_msgs::EmergencyStopState out_pub_em_stop_state_;
    std_msgs::Float64 out_pub_voltage_;
    std_msgs::Float64 out_pub_current_;
};

//document how this class has to look
//never change after first generation
class cob_voltage_control_impl
{

public:

    //CPhidgetInterfaceKitHandle IFK;
    cob_voltage_control_impl()
    {
        //user specific code
    }
    void configure()
    {
    }
    void update(cob_voltage_control_data &data, cob_voltage_control_config config)
    {
        //user specific code
        //Get Battery Voltage
        double voltage_raw = 0;
        voltage_raw = data.in_phidget_voltage;
        //Get Battery Current
        double current_raw = 0;
        current_raw = data.in_phidget_current;

        ROS_DEBUG("voltage_raw: %f", voltage_raw);
        ROS_DEBUG("current_raw: %f", current_raw);

        //Calculation of real voltage
        //max_voltage = 50V ; max_counts = 999
        //from measurements: 49.1 V => 486 counts
        double max_counts = 693.0; // 3v => max
        double voltage = voltage_raw * config.max_voltage_res/max_counts;
        data.out_pub_voltage_.data = voltage;
        ROS_DEBUG("voltage %f", voltage);

        //current calculation
        //500 counts => 0 A
        //999 counts => 2.5 A
        //000 counts => -2.5 A
        double count_min = 611;
        double count_max = 450;
        double v_min = -3.0;
        double v_max = 1.6;
        
        double current = v_min+(v_max - v_min)*(current_raw-count_min)/(count_max - count_min);
        data.out_pub_current_.data = current;
        ROS_DEBUG("current %f", current);
        
        bool charging;
        if (current > 0){charging = true;}
        else {charging = false;}

        //Linear calculation for percentage
        double percentage =  (voltage - config.min_voltage) * 100/(config.max_voltage - config.min_voltage);
        percentage = std::min(percentage, 100.0);

        data.out_pub_power_state_.header.stamp = ros::Time::now();
        data.out_pub_power_state_.voltage = voltage;
        data.out_pub_power_state_.current = current;
        data.out_pub_power_state_.power_consumption = voltage * current;
        data.out_pub_power_state_.relative_remaining_capacity = percentage;
        data.out_pub_power_state_.charging = charging;

    }

    void exit()
    {
    }

};