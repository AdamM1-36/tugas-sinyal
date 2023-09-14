#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:01:14 2023

@author: adam
"""

import numpy as np
from matplotlib import pyplot as plt

# Function to generate sine wave using params: amplitude, frequency, time axis
def generate_sine_wave(amplitude: float, frequency: float, dt: np.ndarray):
    return amplitude * np.sin(2 * np.pi * frequency * dt)

# Assign carrier and message wave characteristics
carrier_amplitude: float = 500
carrier_frequency: float = 1000
message_amplitude: float = 300
message_frequency: float = 60

# Time axis, from 0 to 0.1s with 1000 partition
time = np.linspace(start= 0, stop= 0.1, num= 1000)

# Main program
if __name__ == '__main__':
    # Generate carrier and message signal
    carrier_signal = generate_sine_wave(carrier_amplitude, carrier_frequency, time)
    message_signal = generate_sine_wave(message_amplitude, message_frequency, time)
    
    # Generate AM signal using modulation mathematical expression 
    # (carrier_amplitude + message_signal)*sin(2*pi*carrier_freq*t)
    # which means, the amplitude of carrier signal is modulated.
    # Message signal amplitude is enveloping the carrier signal
    modulated_signal = generate_sine_wave(
        (carrier_amplitude + message_signal),
        carrier_frequency,
        time)
    
    # Create 3 rows plot
    plt.subplot(3,1,1)
    plt.plot(message_signal,color='blue')
    plt.ylabel('Amplitude')
    plt.xlabel('Message signal')
    
    plt.subplot(3,1,2)
    plt.plot(carrier_signal, color='red')
    plt.ylabel('Amplitude')
    plt.xlabel('Carrier signal')
    
    plt.subplot(3,1,3)
    plt.plot(modulated_signal, color="purple")
    plt.ylabel('Amplitude')
    plt.xlabel('AM signal')
    
    plt.rc('font', size=22)
    # get current figure as Figure object
    fig = plt.gcf()
    # subplot title doesn't show when using default hspace = 0.2 (vertical space is too tight)
    fig.subplots_adjust(hspace=0.4)
    fig.set_size_inches(16, 10)
    
    # Save figure
    fig.savefig('AM.jpg')
    
    print("Nama: Adam Mahendra")
    print("NRP: 5009211069")