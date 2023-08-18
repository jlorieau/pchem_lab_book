Labworks
********

Audrey Dell Hammerich, Luke Hanley, and Preston Snee
Yoshitaka Ishii, Sanja Tepavcevic, and Ben Stokes

Introduction
============

Thermodynamics
--------------

Almost all chemical reactions either absorb or release heat. These experiments
are designed to introduce you to three concepts of thermodynamics:

1) The measurement of heat energy

2) In a closed system, the heat gained by one object must equal the heat lost
   by another.
3) Energy is liberated or absorbed (as heat) during physical and chemical
   changes.

Heat and temperature are not the same. When heat is added to a substance, the
temperature rises, but the amount of temperature rise depends on the type and
quantity of substance. Temperature depends on heat, but is not directly or
simply a measure of the amount of heat. You feel that something is hot or
cold, because either it transfers heat to you or you to it.

Temperature is a measure (in degrees) of the average rate of motion of
molecules in a substance. Heat energy is often measured in calories. The
calorie is the amount of heat required to raise the temperature of exactly
1 gram of water from 14.5°C to 15.5°C. For all practical purposes, the calorie
is simply defined as the amount of heat required to raise the temperature of
1g of water 1°C.

The amount of heat required to raise 1 g of a substance 1°C in temperature is
called the specific heat of the substance. Specific heat is a characteristic
property, just like density or boiling point.

.. Examples of How Heat Loss and Heat Gain Are Used in Everyday Life

The combustion of natural gas in a water heater, furnace, or modern power
plant is a common heat-producing (exothermic) reaction. Natural gas is
mostly methane, CH4. The combustion of methane results in the following
reaction:

Objectives
----------

1. Define the concepts of specific heat
2. Compare changes in energy for chemical and physical processes
3. Perform heat-gain and heat-loss calculations
4. Explore real-world examples of heat-gain and heat-loss
5. Define the effects of temperature, pressure and volume of gases
6. Determine the effect of temperature and pressure on the volume of a gas
7. Graphically deduce Boyle's law and Charles's law
8. Apply the gas laws to real-world examples

Set up
======

Thermistor calibration
----------------------

This tutorial explains how to do temperature measurements using the DataMate
program in Time Graph mode on a TI graphing calculator connected to a LabPro
interface with a temperature probe. The LabPro interface reads signals from a
variety of sensors and transmits those signals electrically to a calculator or
computer.

Sensors can be divided into two basic types—analog and digital. Examples of
analog sensors are temperature probes, pH sensors, force sensors, oxygen gas
sensors, etc. Up to four analog sensors can be connected to LabPro. Four jacks
for the analog sensors (CH 1 – CH 4) are located on the same side as the AC
adapter port. The analog ports accept British Telecom-style plugs with a
right-hand connector. Examples of digital sensors are motion detectors,
radiation monitors, photogates, and rotary motion sensors. Up to two digital
sensors can be connected to LabPro. The digital ports (DIG/SONIC), which
accept British Telecom-style plugs with a left-hand connector, are located
on the same side as the serial and USB computer connections.

.. figure:: figures/vernier_labpro_diagram.png

    Diagram of the compoments for the Vernier LabPro [Vernier]_.


1.  *Plug the link cable into the link port of the TI graphing calculator and
    LabPro*. You will collect data on TI graphing calculator and use LabPro only
    as an interface (I/O port).

2.  *Plug the stainless-steel temperature probe into Channel 1*
    Connect the sensor to the appropriate port (Channel 1 for temperature probe).
    An important feature of LabPro is its ability to detect auto-ID sensors,
    and automatically set up an experiment.

    .. note::

        Remember that the temperature probe does not need calibration, so skip
        any instructions asking you to calibrate the sensor!

3.  *Provide power to LabPro (AC adapter)*
    To use LabPro with the AC power supply, plug the round plug on the 6-volt
    power supply into the side of the interface. Shortly after plugging the
    power supply into the outlet, the interface will run through a self-test.
    You will hear a series of beeps and blinking lights (red, yellow, then
    green) indicating a successful power up. If the self-test is not
    successful, unplug everything and plug it in again. You cannot proceed
    until you hear the beeps!

4.  *Start the DataMate program on TI-84 Plus graphing calculator*

    a. Turn the calculator ON

    b. Press APPS (Applications)

    c. Press number under DataMate program

    d. This temporary screen will appear:

       .. image:: figures/vernier_labpro_datamate_screen.png
           :width: 300

    e. After the program begins, the calculator will try to communicate with
       the interface and check for auto-ID sensors. If this communication is
       successful, the main screen (shown below) will appear.

       .. image:: figures/vernier_labpro_mainscreen.png
           :width: 300

    f. In this example a temperature probe was connected and DataMate
       automatically identified and displayed the channel it was connected to,
       giving the current temperature reading. DataMate also sets up a default
       time graph experiment for auto-ID sensors. In this example, an experiment
       was set up to collect data for 180 seconds.

    g. Change the time settings, if needed:

       1. Press 1 (for Setup in Main Menu)

       2. Select Mode and press Enter

       3. In Select Mode menu press number 2 (Time graph)

       4. Select Options and then Change time settings

       5. Pick time interval between the points and total time of the
          experiment (should be the same for all three experiments!)

       6. You are now ready to collect data

5.  *Collect data with DataMate on a TI graphing calculator*. Use the following
    steps to collect data on the DataMate program. Note that the TI calculator
    can only hold a maximum of three sets of data from a single auto-ID sensor
    such as a temperature or pressure probe:

    a. Press 2 (for Start in Main Menu)

    b. When experiment is done (graph will automatically appear) press Enter
       (to go back to Main Menu). If you want to stop experiment run earlier
       click STO>

    c. Press 5 (for Tools in Main Menu)

    d. Press Store Last Run

    e. Repeat it for the second set of data

    f. At the end of the third set of the data there is no need for Store
       Last Run step, instead press 6 (for Quit in Main Menu)
       (last measurement will be stored automatically)

6.  *Transmit data to computer*. Use the following steps to retrieve data from
    the TI calculator by the computer:

    a. All computers have Logger Pro 3.3 software on them

    b. Connect the calculator and the computer I/O (calculator) - USB
       (computer) silver graphing cable

    c. Start Logger Pro 3.3 program by double-clicking on the icon

    d. Click on the little calculator icon in the top line on the program menu
       (Import from TI device should appear when you put mouse on little
       calculator icon)

    e. Pick the TI-GRAPH LINKTM-USB from the Port pull down menu. Skip the
       following step if TI- GRAPH LINKTM-USB is already present.

    f. Click on Scan for device

    g. From Choose data to import, highlight L1 (time) and L2, L3, and L4
       lines (Temperature) by holding Ctrl button

    h. Click OK

    i. You can make:

       1. Single graph (for example only L2 vs. L1)

       2. All three measurements appear on the screen at the same time by
          clicking on the temperature axes (y-axes), choose option More and
          then check the three columns to be displayed (L2, L3, L4)

       3. Click OK

    j. To save graph in format that you can later use with Excel, Origin, or
       MATLAB go to:

       1. File

       2. Export as

       3. Text

    k. Save that text file (\*.txt) on your flash drive

       1. Click No for “Do you want to save changes you made to
          Untitled.cmbl”

    l. Repeat another set of three measurements if needed.

    m. With Excel

       1. Open the Excel program

       2. Under the File pick Open, mark the text file, click OK

       3. Importing text file: click Finished

Experiments
===========


References
==========
.. [Vernier] Vernier LabPro User's Manual, Vernier Software & Technology,
    Beaverton, Oregon. 2013. *url*: http://www2.vernier.com/labpro/labpro_user_manual.pdf