Laser-Induced Fluorescence
**************************

Introduction
============

In this experiment you will measure the decay kinetics of
fluorescence for quinine sulfate in water solutions. Quinine is used as a
fluorescence standard because the fluorescence is not quenched (decreased) by
oxygen but can be quenched in a controlled manner by adding atomic anions
(F\ :sup:`-`, Cl\ :sup:`-`, I\ :sup:`-` and Br\ :sup:`-`) to the
solution [JPhotochem1990]_. We will use a laser to optically excite quinine
and study the kinetics of quenching as a function of Cl\ :sup:`-` anion
concentration.

Energy Levels and Transitions
-----------------------------

The energy levels in a molecule can be broken down into their component
electronic, vibrational and rotational energy levels.

.. math::

    E(n, v, J) = E(n)_{electronic} + E(v)_{vibrational} + E(J)_{rotational}

The Boltzmann distribution tells us that at room temperature, molecules only
occupy the *ground state* for electronic and vibrational energy levels.
Electronic energy levels in a molecule are the Hamiltonian eigenvalues of
*molecular orbitals* (MO) wavefunctions.

Molecules can absorb energy from heat, collisions or photons to populate
excited energy levels. To stimulate an electron from one electronic energy
level (molecular orbital) to another, the molecule must absorb a photon with
the correct frequency (:math:`\nu`)--typically in the UV or visible frequency
range for electronic transitions.

.. math::

    h \nu = \Delta E = E_{excited} - E_{ground}

.. admonition:: Electronic energy level multiplicities
    :class: note

    Electronic energy levels come in a few varieties based on electron spin
    multiplicities. The number of electronic states can be counted from the net
    electron spin angular momentum of a molecule, S, with the formula: 2S + 1.
    Diamagnetic molecules, like water or quinine, have an equal number of
    electrons in molecular orbitals with a spin up (:math:`m_s = 1/2`), as
    there are electrons with spin down (:math:`m_s = -1/2`). The net electron
    spin angular momentum is zero (S = 0) such that there is only a single
    electronic state--*i.e.* a singlet 'S' state. Radical molecules have 1
    unpaired electron in molecular orbitals with a net electron spin angular
    momentum S = 1/2 such that there are two degenerate electronic
    states--*i.e.* a doublet 'D' state. Molecules with two unpaired electrons
    with the same spin have a net angular momentum S = 1 such that there are
    three degenerate electronic states--*i.e.* a triplet 'T' state. The
    energy levels become non-degenerate in a magnetic field.

In absorption spectroscopy of diamagnetic molecules, we study electronic
transitions from a ground singlet electronic energy level (S\ :sub:`0`),
the Highest Occupied Molecular Orbital (HOMO), to an excited singlet
electronic energy level (S\ :sub:`1`), the Lowest Unoccupied Molecular Orbital
(LUMO). These transitions are commonly illustrated with a Jablonski diagram.

.. figure:: figures/Jablonski/jablonksi.png
    :alt: Example Jablonski diagram for a molecule

    An example Jablonski diagram.

At room temperature, electrons in diamagnetic molecules are paired and start
in the ground singlet HOMO (S\ :sub:`0`) state and ground vibrational state
(v=0). An electron may **absorb** a photon of the correct frequency to an
excited singlet LUMO state (S\ :sub:`1`) and excited vibrational state--in
the above diagram the molecule is excited to the v=3, v=2 and v=1 vibrational
levels with photons of different frequencies and energies. Thereafter, the
molecule relaxes by **non-radiative** or **vibrational relaxation** through
collisions with other molecules.

In the excited electronic state, the molecule may:

1.  **internally convert** to an excited vibrational state of the ground
    electronic state (S\ :sub:`0`) and continue to lose energy non-radiatively
    (*i.e.* without emiting a photon) until the system has reached the ground
    vibrational state (v=0).

2.  **fluoresce** by emitting a photon and populating an excited vibrational
    state of the ground electronic state (S\ :sub:`0`). Thereafter, the system
    continues to lose energy non-radiatively until the system has reached the
    ground vibrational state (v=0).

3.  **intersystem cross** to triplet states, lose energy non-radiately, then
    slowly **phosphoresce** back to an excited vibrational state of the ground
    electronic state (S\ :sub:`0`), before losing energy non-radiatevely to the
    ground vibrational state (v=0).

Some or all of these relaxations mechanisms may be available, depending on the
molecule, and the prevalence of each also depend on the kinetics of each
process. Absorption typically occurs on a femtosecond (10\ :sup:`-15` s)
timescale, or the timescale it takes a photon to travel one wavelength. The
other relaxation processes occur on a slower timescale:
vibrational relaxation (*ca.* 10\ :sup:`-11`-10\ :sup:`-9` s),
fluorescence (*ca.* 10\ :sup:`-8`-10\ :sup:`-4` s) and
phosphorescence (*ca.* 10\ :sup:`-4`-10\ :sup:`2` s) [Harris]_.

.. dropdown:: Selection rules and the Frank-Condon Principle
    :color: info
    :icon: info

    The electric field component of photons interact with the electric
    dipoles of molecules. The electric dipole can be measured
    from the expectation value of the molecules wavefunctions. To simplify the
    discussion, we will only focus on the electric dipole and that depends on
    the electron coordinates, :math:`\mu_e`.

    .. math::

        \langle \mu \rangle = \langle \psi_e (n') \psi_v (n', v') \rvert \hat{\mu_e} \lvert \psi_e (n) \psi_v (n, v) \rangle

    In this case, we will focus on the electronic states (:math:`\psi_e`) and
    vibrational states (:math:`\psi_v`) that impact the expectation value.
    The vibrational states only depend on the nuclear coordinates--*i.e.* it
    does not interact with the electric dipole from electron coordinates--and it
    can be factored.

    .. math::
        :label: eq_franck-condon

        \langle \mu \rangle = \boldsymbol{\langle \psi_v (n', v') \vert \psi_v (n, v) \rangle} \langle \psi_e (n')  \rvert \hat{\mu_e} \lvert \psi_e (n)  \rangle

    The second bracket (not in bold) represents the transition from an electronic
    state :math:`n` to a different electronic state :math:`n'` when a molecule
    absorbs a photon. It is for this reason that we name the above the
    **transition electric dipole** since it describes the transition from
    one electronic state from another. The electric dipole moment operator,
    :math:`\hat{\mu}`, may not commute with the eigenbasis of the Hamiltonian,
    and it may change the eigenstates :math:`n` to a new set of eigenstate,
    :math:`n'`. This bracket's integral follows the electronic transition
    selection rules.

    Discussion of the the vibrational component requires a bit of background.
    In vibrational (IR) spectroscopy, we evaluated the transition electric
    dipole for the nuclear coordinates, :math:`\mu_n`, and we found that
    the following selection rule for vibrational transitions:
    :math:`v' = v \pm 1`. These were for vibrational transitions in the ground
    electronic state.

    In electronic spectroscopy, we are inducing electronic transitions from
    state :math:`n` to state :math:`n'`. Electrons are excited into
    non-bonding or anti-bonding molecular orbitals, which can have a different
    bond order, bond length and vibrational properties than the ground state
    molecule. For this reason, the vibrational states also depend on the
    electronic state, :math:`\lvert \psi_v (n, v) \rangle`.

    The vibrational eigenstates are orthogonal within a given electronic state.

    .. math::

        \langle \psi_v(n,v') \vert \psi_v(n, v) \rangle = 0 \qquad \text{when } v \neq v' \\
        \langle \psi_v(n,v') \vert \psi_v(n, v) \rangle = 1 \qquad \text{when } v = v'

    In equation :eq:`eq_franck-condon`, the first bracket in bold is the
    *Franck-Condon factor*, F.

    .. math::

        \langle \psi_v (n', v') \vert \psi_v (n, v) \rangle = F

    F may be non-zero for many excited vibrational
    states in the excited electronic state. Since :math:`n \neq n'` for
    electronic transitions, these eigenfunctions are not orthogal when
    :math:`v \neq v'`. This means that for an electronic transition from
    :math:`n` to :math:`n'`, vibrational transitions from :math:`v = 0` to
    :math:`v' = 1, 2, 3, 4,` etc. may be possible. The probability of these
    transitions dependent on the magnitude of the Franck-Condon factor integral.

    See section 5-4 in [Harris]_ for a more detailed discussion on selection
    rules and the Franck-Condon factor.

Fluorescence
------------

Fluorescence is the process by which molecules emit a photon when relaxing
from an excited electronic singlet state (S\ :sub:`1`). Vibrational relaxation
in the excited state before emission (S\ :sub:`1`) and in the ground electronic
state after emission (S\ :sub:`0`) reduces the energy of the emitted photon.

.. math::

    E &= h \nu \\
    E_{absorbed} &> E_{fluoresced}

Consequently, the emitted photon has a lower frequency and a larger wavelength
than the absorbed photon

.. math::

    \nu_{absorbed} &> \nu_{fluoresced} \\
    \lambda_{absorbed} &< \lambda_{fluoresced}

Photons in the visible spectrum shift to higher wavelengths toward photons that
are red in color (*ca.* 600 nm). For this reason, we say that fluoresced
photons are *red shifted* from the absorbed photon. This phenomenon is known
as the **Stokes shift**.

From a practical perspective, fluorescence spectroscopy is more *sensitive*
than absorbance spectroscopy. Absorbance spectroscopy measures the
fraction of photons that have transmitted through the sample, by measuring
light in the path of the light source. Very small amounts
of absorbance--*e.g.* 1 photon in 1 million-- can be difficult to detect,
particularly if the light source does not have a stable intensity.
Fluorescence is measured at a right angle from the light source, and every
photon detected can be guaranteed to have come from a fluorescing molecule.
Consequently, the lower noise threshold produces much lower limits of
detection (LOD) for fluorescence experiments in comparison to absorbance
experiments.

Time-Resolved Fluorescence and Quenching
----------------------------------------

Fluorescence can be inhibited by a quencher. Quenchers that are
effective for some fluorophores may not be effective for others,
and many quenching mechanisms exist [Lakowicz]_. The two main
categories of fluorescence quenching are *dynamic quenching* and
*static quenching*.

In the absence of a quencher, fluorescence follows a relatively simple kinetic
scheme.

.. figure:: figures/kinetics/kinetics.png
    :width: 450
    :alt: Kinetic schemes for fluorescence, dynamic quenching and static quenching

    Kinetic schemes for fluorescence, dynamic quenching and static quenching

A fluorophore (F) absorbs a photon (hv\ :sub:`a`) at a rate
k\ :sub:`a`. The excited fluorophore (F\ :sup:`*`) may emit a red-shifted photon
(hv\ :sub:`f`) at a rate k\ :sub:`f` or the molecule may relax non-radiatively
at a rate k\ :sub:`nr`. The rate of excited fluorophore and intensity of
fluoresced photons (hv\ :sub:`f`) can be written as follows:

.. math::
    :label: fluoro-full-rate

    \frac{d[F^*]}{dt} = - \frac{d[h \nu_f]}{dt} = k_a [F][h \nu_a] - k_f [F^*] - k_{nr} [F^*]

The rates depend on concentrations, and we've labeled the incoming intensity
or number of absorbed photons as a concentration, :math:`[h \nu_a]`, like a
chemical reagent in a reaction. This notation is commonly employed in
laser-induced chemistry [Gutow]_. This can be thought as the number of photons
in a volume of solvent, which is directly proportional to the intensity of the
light source, and it becomes zero when the light source is turned off.

A light pulse from a laser creates excited fluorophores, [F\ :sup:`*`]. Once
the the laser light is shut off, :math:`[h \nu_a] = 0`.

.. math::
    :label: fluoro-rate

    \frac{d[F^*]}{dt} &= - (k_f + k_{nr}) [F^*] \\
    &= - k' [F^*]

In this equation, we cannot distinguish the rate of fluorescence (k\ :sub:`f`)
and the rate non-radiative emission (k\ :sub:`nr`), so these are grouped
together into a new excited fluorophore decay rate, k'.

The rate equation can be integrated.

.. math::

    \int_{[F^*(0)]}^{[F^*(t)]} \frac{d[F^*]}{[F^*]} &= - \int_0^t k' dt \\
    \ln \frac{[F^*(t)]}{[F^*(0)]} &= - k' t

Rearranging the equation yields a mono-exponential decay.

.. math::
    :label: fluoro-monoexp

    [F^*(t)] = [F^*(0)] e^{- k' t}

The concentration of the excited fluorophore can be calculated at time 't',
:math:`[F^*(t)]`, after the laser pulse. It depends on the concentration of
excited fluorophore immediately after the laser pulse, :math:`[F^*(0)]`.
In practice, we do no measure this concentration directly, but we infer this
concentration from the number of fluorescent photons measured.

.. math::

    [F^*] \propto [h \nu_f] \propto I_{fluorescence}

The mono-exponential from equation :eq:`fluoro-monoexp` can be measured
from the intensity of fluorescence after the laser pulse.

.. math::
    :label: fluoro-monoexp-intensity

    I(t) = I(0) e^{-k' t}

**Dynamic quenching**. Incorporating a quencher modifies the kinetics of
fluorescence decay. Collision with a dynamic quencher (Q) produces a new
non-radiative pathway that depends on the concentration of the quencher, adding
another term to equation :eq:`fluoro-rate`.

.. math::

    \frac{d[F^*]}{dt} = -k' [F^*] - k_Q [Q][F^*]

Integrating and rearranging as we did before creates a new function that depends
on the concentration of the quencher, [Q].

.. math::
    :label: fluoro-dynamic-quench

    I(t) &= I(0) e^{-(k' + k_Q[Q])t} \\
         &= I(0) e^{-k_{app}t}

The apparent rate of decay, k\ :sub:`app`, now depends on the concentration of
the quencher.

.. math::
    :label: fluoro-dynamic-rate-constant

    k_{app} = k' + k_Q [Q]

.. admonition:: Rates of dynamic quenching
    :class: note

    The fastest rate a (bimolecular) reaction can take place between two
    molecules in solution is limited by the diffusional rate, k\ :sub:`D`.
    (Molecules can't react faster than the time it takes them to collide into
    each other)

    The diffusion controlled rate can be estimated from a derivation of the
    Stokes-Einstein rate of diffusion [PhysicalChemistry]_.

    .. math::
        :label: diffusion-controlled

        k_D = \frac{8RT}{3 \eta}

    The viscosity (:math:`\eta`) of water at room temperature
    (T = 298K) is 1.0 centipoise
    (:math:`1 cP = 10^{-3} Pa \cdot s = 10^{-3} kg \cdot m^{-1} s^{-1}`).
    The rate constant for diffusion in water at room temperature can be
    calculated.

    .. math::

        k_D = \frac{8(8314 L \cdot Pa \cdot K^{-1} mol^{-1})(298K)}{3 (10^{-3} Pa \cdot s)} = 6.6 \cdot 10^9 M^{-1} \cdot s^{-1}

    Of course, other effects might be at play such as electrostatic forces
    between diffusing ions.

    For neutral molecules, the dynamic quenching rate is equal or smaller
    than the rate constant for diffusion, :math:`k_D \geq k_Q`. In the case
    that they're equal, all collisions between a dynamic quencher and a
    fluorophore lead to a quenching event.

**Static quenching**. Static quenchers are molecules that "trap" the ground
state fluorophore into a complex that cannot fluoresce, :math:`[F \cdot Q]`.
Effectively, static quenchers diminish the concentration of fluorophore
molecules that can fluoresce, :math:`[F]`.

.. math::

    [F]_0 = [F] + [F \cdot Q]

The initial or total concentration of fluorophore, :math:`[F]_0`, is
distributed between the free fluorophore, :math:`[F]`, and the fluorophore
complexed to the static quencher, :math:`[F \cdot Q]`. The binding of the
static quencher can be described by an equilibrium with an equilibrium
constant, :math:`K_{eq}`.

.. math::

    K_{eq} = \frac{[F-Q]}{[F][Q]}

We can combine the two equations.

.. math::

    K_{eq} = \frac{[F]_0 - [F]}{[F][Q]}

And solve for the concentration of free fluorophore, :math:`[F]`:

.. math::
    :label: static-quench-conc

    K_{eq}[F][Q] &= [F]_0 - [F] \\
    [F] &= \frac{[F]_0}{K_{eq}[Q] + 1}

When the concentration of the static quencher is zero, :math:`[Q] = 0`, or
the "quencher" does not interact with the unexcited fluorophore,
:math:`K_{eq} = 0`, the the concentration of the fluorophore is equal to the
initial or total concentration of fluorophore, :math:`[F] = [F]_0`.

When looking at the kinetic equation :eq:`fluoro-full-rate` for fluorescence,
the difference in unexcited fluorphore concentration only impacts the first
term.

.. math::

    \frac{d[F^*]}{dt} =  k_a [h \nu_a] \frac{[F]_0}{K_{eq}[Q] + 1} - k' [F^*]

However, immediately after the laser pulse when :math:`[h \nu_a] = 0`, the rate
equation appears identical to fluorescence without a quencher.

.. math::

    \frac{d[F^*]}{dt} =  - k' [F^*]

And the intensity decay of the fluorescence follows the same mono-exponential.

.. math::

    I(t) &= I(0) e^{-k' t} \\
         &= I(0) e^{-k_{app}t}

The apparent rate of decay, k\ :sub:`app`, does not depend on the concentration
of the quencher.

.. math::
    :label: fluoro-static-rate-constant

    k_{app} = k'

So then how can we tell a static quencher from a non-quenching molecule? The
fluorescence decay rate is the same as it was without the quenching molecule,
but the initial fluorescence intensity, I(0), is reduced because there are
fewer fluorescent molecules.

.. math::

    [F^*] \propto [F] \propto I_{fluorescence}

.. admonition:: Example fluorescence decay curves for different quenchers
    :class: note

    The following shows example fluorescence intensity decays after a laser
    pulse for different types of quenchers.

    .. plot::

        import numpy as np
        import matplotlib.pyplot as plt
        plt.figure(figsize=(5, 3.5))

        plt.xlabel("time (ns)")
        plt.xlim(0.0, 1000.)

        plt.ylabel("Intensity (A.U)")
        plt.ylim(0.0, 1.05)

        t = np.arange(0.0, 1000., 2.0)  # nanoseconds

        kf = 3.0E6  # s^-1
        Iref = np.exp(-kf * t * 1E-9)
        plt.plot(t, Iref, label='no quencher')

        Qconc = 0.001  # molar
        kQ = 1.0E9  # M^-1 s^-1
        Idyn = np.exp(-(kf + kQ * Qconc) * t * 1E-9)
        plt.plot(t, Idyn, label='dynamic quencher')

        Keq = 1000. # M^-1
        Istatic = (Keq * Qconc + 1.0) ** -1. * np.exp(-kf * t * 1E-9)
        plt.plot(t, Istatic, label='static quencher')

        plt.legend()
        plt.tight_layout()

    In all three plots, the effective decay rate, :math:`k'`, is
    :math:`3 \cdot 10^6 s^{-1}`. The fluorescence decay without quencher
    was modeled with equation :eq:`fluoro-monoexp-intensity`. The
    fluorescence decay with dynamic quencher was modeled with equation
    :eq:`fluoro-dynamic-quench`, a quencher concentration [Q] = 1.0 mM
    and a quencher rate :math:`k_Q = 10^9 M^{-1} s^{-1}`. The fluorescence
    decay with static quencher was modeled with equation
    :eq:`fluoro-monoexp-intensity` and an initial intensity scaled by equation
    :eq:`static-quench-conc` with a quencher concentration [Q] = 1.0 mM
    and a quencher equilibrium constant :math:`K_{eq} = 1000 M^{-1}`.

Continuous Fluorescence and Quenching
-------------------------------------

Fluorescence experiments are also commonly measured in continuous
mode--that is, without resolving the time dependency of the intensity
decay. In continuous experiments, the light source is *continuously*
turned on and the fluorophore is *continuously* absorbing photons.
The rate equation :eq:`fluoro-full-rate` for the fluorophore must be
updated accordingly.

.. math::

    \frac{d[F^*]}{dt} = 0 = k_a [F][h \nu_a] - k' [F^*]

As long as the light source intensity remains constant and time independent,
there are two changes:

#. The excited fluorophore concentration stops changing
   such that :math:`\frac{d[F^*]}{dt} = 0` and the concentration reaches a
   *steady-state*, constant concentration, [F\ :sup:`*`].

#. The light source is continuously turned on so :math:`[h \nu_a]` is no longer
   zero.

The steady-state concentration of the excited fluorophore, [F\ :sup:`*`]\ :sub:`ss`, can
be calculated without quencher.

.. math::

    [F^*] = \frac{k_a}{k'} [F]_0 [h \nu_a ]

Here we recognized that the unexcited fluorophore concentration is equal to the
initial or total concentration, :math:`[F] = [F]_0`.

In the presence of a *dynamic quencher*:

.. math::

    [F^*] = \frac{k_a}{(k' + k_Q[Q])} [F]_0 [h \nu_a ]

and dividing by :math:`[F^*]` without quencher yields the Stern-Volmer
equation.

.. math::
    :label: stern-volmer

    \frac{[F^*]_{0}}{[F^*]} = \frac{k' + k_Q[Q]}{k'} = 1 + k_Q \tau_0 [Q]

In the last equation, we made use of :math:`\tau_0 = k'^{-1}`, which is the
lifetime of the excited state. The lifetime, as with k', depends on the rate
of fluorescence and the rate of non-radiative emission.

In the presence of a *static quencher*:

.. math::

    [F^*] = \frac{k_a}{k'(K_{eq}[Q] + 1)} [F]_0 [h \nu_a ]

and dividing by :math:`[F^*]` without quencher yields an equivalent
varient of the Stern-Volmer equation.

.. math::

    \frac{[F^*]_{0}}{[F^*]} = 1 + K_{eq} [Q]

Plotting the concentration of the quencher, [Q], against the factor reduction
in fluorescence intensity, :math:`\frac{[F^*]_{0}}{[F^*]}`, from the quencher
yields a linear equation for dynamic and static quenchers. For the former, the
slope is :math:`k_Q \tau_0` and for the latter the slope is :math:`K_{eq}`. Both
have an intercept of 1.0.

Altogether, the Stern-Volmer equation and continuous fluorescence can be used
to identify whether a molecule is a quencher. Unfortunately, it's not useful
in distinguishing between a dynamic and a static quencher.

Oxygen Quenching
----------------

Oxygen, :math:`\ce{O2}`, is a paramagnetic molecule that is a very effective
*dynamic quencher* in many fluorophores. The concentration of dissolved
oxygen can be variable and difficult to determine in a solution. The net effect
of oxygen's quenching is to increase the apparent rate, k', and reduce the
lifetime of the excited state, :math:`\tau_0`. This reduction in the accuracy
of the rate can by circumvented by purging as much dissolved :math:`\ce{O2}`
as possible--either by placing the solution in a weak-to-moderate vacuum or
bubbling :math:`\ce{N2}` gas in the solution.

Experimental Setup
------------------

You will use a laser, a monochromator, a photomultiplier tube (PMT) and a
digital storage oscilloscope to collect the time-resolved, laser-induced
fluorescence of quinine sulfate at approximately 10-5 M and 0.5 M
:math:`\ce{H2SO4}` in water. You will observe the effects of :math:`\ce{Cl-}`
as a quencher by varying its concentration in the solution.

.. figure:: figures/expt_setup/expt_setup.png

    Block diagram of the laser, monochromator, photomultiplier tube (PMT) and
    oscilloscope used in the experimental procedure. The experimental setup
    includes lenses (L), filters (F1, F2), a beam splitter (B), mirrors (M1-M4),
    slits (S1, S2) and a grating (G).


**N2 laser**. The N\ :sub:`2` gas laser produces photons in the
ultraviolet range (337.1 nm). The output from the laser is split by
beamsplitter (B). Part of the laser beam is focused by lens (L) onto the
sample cuvette while the other part passes through a neutral density filter
(F1) to reduce its intensity and strikes a photodiode, triggering data
acquisition by the digital oscilloscope.

**Monochromator**. A monochromator separates the frequencies of photons that
are combined in the incoming light. After the laser beam travels through the
sample, we use the monochromator to select a narrow range of frequencies for
the fluoresced (emitted) light by the same.

In the experimental setup, the fluorescence is collected at right angles
to the incoming laser beam, passes through a neutral density filter (F2),
and then into the monochromator. The monochromator is an Ebert optical mount.
The light passes through the entrance slit S1, striking a 45\ :sup:`o`
mirror (M1), and is reflected to a large collimating mirror M2. From this
mirror it is it is reflected to the grating (G) and dispersed back to the
collimating mirror (M3). The light beam, returning to focus, is reflected by a
45\ :sup:`0` mirror (M4) out through exit slit (S2) and into the
photomultiplier housing.

The monochromator should be set to detect 480 nm fluorescence. This is far
from the laser frequency of 337.1 nm and is the frequency at which the
fluorescence exhibits simple exponential decay. At other wavelengths the
emission rate is affected by a number of other processes that have not been
considered, and requires a sum of two or more exponential functions to fit
the decay [Barrow]_. If there is time, you might want to collect fluorescence at
about 390 – 400 nm from a sample without quencher to see if the
biexponential decay can be observed.

**Photomultiplier Tube**. The light that gets through the monochromator is
detected by a photomultiplier tube (PMT). PMTs are based on the
photoelectric effect. After a light photon ejects an electron from the
photocathode the electron is accelerated by a potential voltage into
another electrode. The accelerated electron knocks many electrons out of
the electrode, which are then accelerated to another electrode. This
process is repeated 9 times here (9 stage PMT) giving a current gain
of about 10\ :sup:`6` – 10\ :sup:`7`! With a PMT, it is possible to
see the signal from a single photon; if you have a 350 MHz or greater
oscilloscope and the fluorescence intensity is low enough you may be
able to see individual spikes (photons) in the decay signal from the
PMT.

.. danger::

    Typically PMTs operate at a negative voltage of between 500 and 1250 V.
    Be very careful: high voltages are dangerous and a PMT can be easily damaged
    by exposing it to too much light while voltages are applied. To avoid
    damaging the PMT do not apply voltage to the tube until the room lights
    are off and start looking for signal at a low voltage increasing the
    voltage only enough to get a signal of a few hundred millivolts at its
    peak. DO NOT TURN THE VOLTAGE ABOVE 800 V! If you have any questions,
    consult with teaching staff.

**Oscilloscope**. Oscilloscopes are instruments that display varying voltages
as a function of time. They often used to analyze, diagnose and characterize
the frequency and amplitudes of signals in industrial and laboratory settings.
Digital oscilloscopes, as used here, use an analog-to-digital converter (DAC)
to digitize analog voltage signals at regular intervals and convert these
to a digital file format that can be analysed on a computer.

.. admonition:: Digital sampling and the Nyquist frequency
    :class: note

    Since the signal is sampled at regular intervals, :math:`\Delta t`, changes
    in the signal that are *faster* than this interval will either be missed
    or "aliased" giving an incorrect frequency measurement. This limitation is
    commonly expressed as an upper limit of the frequencies measured, known as
    the *Nyquist frequency*.

    .. math::

        \nu_{Nyquist} = \frac{1}{2 \Delta t}

    The factor of 2 arises arises because the range of frequencies measured,
    the spectral width, extends to positive and negative frequencies. For
    example, a sample rate of 1 ms can sample frequencies between -500 Hz and
    500 Hz.

The oscilloscope only displays data when told to do so by the occurrence of a
trigger. In this experiment a small amount of the light pulse out of the
laser is used to trigger the beginning of data collection via the photodiode.
This is done since the signal of interest only occurs over a very brief period
of time right after the laser pulse. Mounds of noise (useless data) would be
collected were the signal from the PMT collected at other times.

Procedures
==========

Read and prepare all of the following instructions before starting. Carefully
follow the instructions and particularly the alerts.

Materials
---------

- 1M |H2SO4| solution
- 150 mM KCl stock solution *or* KCl\ :sub:`(s)`
- 25 uM quinine sulfate in 0.5 M |H2SO4| stock solution *or* quinine sulfate (solid)
- Laser table with N2 laser, monochromator, PMT
- Oscilloscope

A. 150 mM KCl stock solution, 500 mL
------------------------------------

(Use an existing solution if it is already prepared, and note the solution
reference in your notebook)

#.  | Add _________ (tgt: 5.59 g) KCl powder to reach a 150mM F.C.
    | FW: 74.55 g/mol
    | Ref:

#.  Add ~250 mL of |ddH2O| and swirl to disolve the KCl powder

#.  Top up to a final volume of 500 mL with |ddH2O|

B. 0.5M |H2SO4| stock solution, 500 mL
--------------------------------------

(Use an existing solution if it is already prepared, and note the solution
reference in your notebook)

.. danger::

    Use gloves and work inside of a fumehood

    Do not add water to acid. Drop-by-drop, add acid to a large volume of water.

#.  Add 400 mL of |ddH2O|

#.  | Add _________ (tgt: 6.9 mL) of concentrated sulfuric acid
      (36 N, |H2SO4|) to reach a 0.5M F.C.

#.  Top up the solution to a final volume of 500 mL with |ddH2O|


C. 25 uM quinine sulfate in 0.5M |H2SO4| stock solution, 100 mL
---------------------------------------------------------------

(Use an existing solution if it is already prepared, and note the solution
reference in your notebook)

#.  | Measure 100 mL of 0.5M |H2SO4|
    | Ref:

#.  | Add _________ (tgt: 2.0 mg) quinine sulfate dihydrate powder to reach a
      25 uM F.C.
    | FW: 782.9 g/mol
    | Ref:


D. 10uM quinine sulfate in 0-40mM KCl samples, 5x5 mL:
------------------------------------------------------

#.  | Add 2.0 mL of 25 uM quinine sulfate in 0.5M |H2SO4|
    | Ref:

#.  | Prepare and label the following 5 samples by adding 150 mM KCl and
      0.5M |H2SO4|:
    | Ref:

    .. list-table::
        :header-rows: 1

        * - Actual 150 mM KCl
          - Target 150 mM KCl
          - F.C. KCl (mM)
          - Actual 0.5M |H2SO4|
          - Target 0.5M |H2SO4|
        * -
          - 1.33 mL
          - 40 mM
          -
          - 1.67 mL
        * -
          - 1.07 mL
          - 32 mM
          -
          - 1.93 mL
        * -
          - 0.80 mL
          - 24 mM
          -
          - 2.20 mL
        * -
          - 0.53 mL
          - 16 mM
          -
          - 2.47 mL
        * -
          - 0.27 mL
          - 8 mM
          -
          - 2.73 mL
        * - 0.00 mL
          - 0.00 mL
          - 0 mM
          -
          - 3.00 mL


E. Continuous Fluorescence Spectra
----------------------------------


F. Time-Resolved Fluorescence Experiment
----------------------------------------

.. danger::

    Be careful: the UV pulse produced by the laser can easily damage your eyes

.. warning::

    Wear plastic glasses that do not transmit the laser light

1.  Turn the Oscilloscope on. It will take a few minutes to boot up.

2.  On the front panel of the oscilloscope, in the ``TRIGGER`` section, make
    sure that “CH 2” is selected as the source, “DC” is chosen for the coupling,
    “POS” is chosen for the slope. Make sure that the BNC cable from the
    photodiode is connected to Channel 2 of the oscilloscope and the
    photomultiplier tube (PMT) is connected to Channel 3. Make sure that the
    resistance for Channel 2 is set to 50 :math:`\Omega` (this in the Vertical
    panel of the oscilloscope’s front, on the bottom.)

3.  Turn on channel 2. You should see it on the screen. Adjust the vertical
    scale knob for channel 2 to 200 mV per division. Adjust the horizontal
    scale knob of the oscilloscope to 20.0 ns/division. Make sure that the
    “RUN/STOP” button on the oscilloscope is lit up (running).

4.  Turn the key on the laser to the ``ON`` position. Let it warm up for a few
    moments until the ``CHARGE`` LEF lights up.

5.  Turn the knob labeled ``RATE`` clockwise until it stops (3/4 turn). The
    laser will begin firing at a 20 Hz repetition rate (20 shots/sec).

6.  At this point, there should be a sharp spike on the Oscilloscope screen
    about 5 nanoseconds wide at the base. If you do not see a spike, adjust
    the vertical and horizontal scaling knobs until a spike appears. The
    spike should be about 500 mV tall and 5 ns wide. If you still do not see
    a spike, adjust the “Level” knob on the ``TRIGGER`` panel of the
    oscilloscope. You can see the trigger level represented as an arrow that
    moves up and down to the right of your screen. Ask your TA for help if you
    need assistance with the trigger level. It should be at about 200 mV, and
    the value is displayed at the bottom right corner of the screen in white
    text.

7.  Go to the ``Horiz/Acq`` tab on the top of the screen and choose
    ``Horizontal/Acquisition Setup...``. In this new window, in the Acquisition
    tab, make sure that the “average” button is selected and that the # of
    waveforms being averaged is 50.

8.  There should be a stable laser pulse on the screen with a Gaussian shape.
    Press the ``Run/Stop`` button on the oscilloscope and the waveform should
    remain frozen on the screen. You can stop the laser firing now. Use the
    cursors to determine the full-width at half-max (FWHM) of this laser
    signal. Record this in your lab notebook. The FWHM is the width of the
    signal at half of its maximum height.

9.  Adjust the trigger Level knob until the arrow is at about 1/3 of the
    signal’s height.

10. Save this waveform as you did with the waveforms from the wavefunction
    generator. Make sure to select ``channel 2`` as the source in the waveform
    options tab.

11. Make sure that the cable from the High Voltage Power Supply is connected
    to the high voltage port of the PMT (photomultiplier tube). Ask you TA to
    help if it is not. Turn on channel 3 on the oscilloscope.

.. danger::

    Make sure that the high voltage power supply is off before you proceed.

    Make sure that the laser is not firing.

12. Place the cuvettee with your first sample of 0.0 KCl in the cuvette
    holder sample chamber and replace the sample chamber lid.

13. Make sure the “High Voltage” switch on the High Voltage Power Supply is in
    the off position and then push the “power” swtich to the on position. A
    red light should come on.

.. danger::

    DO NOT turn on the high voltage power supply to the PMT while the sample
    chamber is open. Doing so will destroy the PMT!

14. After a few moments, the white light under “High Voltage” should come on,
    signifying the power supply is warmed up.

15. Make sure all 5 of the ``output voltage`` selection knobs are set to ``0``
    and the ``polarity`` should be set to negative, ``-``. Push the
    ``high voltage`` switch to the “on” position. The red light should come on.

16. Turn the laser ``rate`` knob to the highest level (20 Hz) to begin firing
    the laser again.

17. Set the vertical setting of channel 3 to 10 mV/div. Make sure the
    horizontal scale is at 20 ns/div.

18. Adjust the high voltage power supply ``output voltage`` knobs in increments
    of 100 V (2nd knob from the left) until you start to see a signal on the
    oscilloscope for channel 3. This is the signal from the photomultiplier
    tube (PMT) that should be showing you the fluorescence of quinine. It
    typically takes about 600 V to get a good signal. If you need to exceed
    500 V, turn all voltage knobs to 0, use the first knob from the left to
    apply 500 V, and then use the next knob to apply another 100 V, for a
    total of 600 V.

.. danger::

    DO NOT EXCEED 800 V as this could cause permanent damage to the PMT

19. At the 500-700 V setting of the power supply, a negative voltage signal
    with a minimum of around -20 to -40 millivolts and a full width of around
    70 ns should be seen. Adjust the horizontal position knob on the
    oscilloscope so that the full signal can be seen. This is the fluorescence
    signal you will use for your measurements. Once you have a signal on the
    screen, press the ``RUN/STOP`` button on the oscilloscope to freeze the
    signal on the screen. Turn the “rate” knob on the laser to “0” to stop it
    from firing.

20. Go to the math tab and ``math Setup`` to invert the waveform so that the
    signal is now positive. Choose the ``math 1`` tab, turn its display button
    to ``on``, clear any equation in the equation editor, and click on the
    ``editor`` button. Select the invert button, choose channel 3, and then
    close the parentheses. Math 1 should not be defined as ``INV(Ch2)``. Click
    ok and you should see the inverted math function on the screen. Make sure
    none of the signal goes off the screen. You may have to adjust the scaling
    settings for the math function in the ``position/scale`` menu from the Math
    tab.

21. Change the cursor settings, as you did with the wavefunction generator
    procedure, so that you can measure the math 1 function. From the cursors
    tab, cursors should be ``on``, cursor type should be ``waveform``, and the
    source for cursor 1 and cursor 2 in the cursor setup screen should be
    math 1, or whatever math function you used to invert the signal from
    channel 3.

22. Place one marker at the peak of your fluorescence signal and then another
    marker to the right of it, where the signal reaches about 1/e (37%) of the
    height of the signal’s maximum. The difference of time between cursor
    1 and 2 is shown to you on the right of the screen. This amount of time is
    the approximate lifetime of the fluorescence, from when the signal is at
    its highest until it is almost completely decayed. Record this value for
    comparison to the fitted values you will find later.

23. Save this waveform. Make sure to choose ``math1`` or whichever math
    function you used to invert the signal from channel 3 as the source
    under the ``waveform options`` menu after you click ``save as``. Remember
    to save in CSV format.

24. To proceed to another trial, being firing the laser again and press the
    ``Run/Stop`` button on the oscilloscope to begin collecting data again.
    Press ``Run/Stop`` again to freeze a new signal on the screen to measure
    its lifetime and save it.

25. When you have acquired 3 trials for one of your samples, stop the laser
    from firing and **turn all knobs on the high voltage power supply to zero
    and turn the ``high voltage`` toggle switch to OFF**. You can now open
    the sample chamber and get three trials of data for the rest of your samples.

.. danger::

    Make sure to stop the laser from firing in between measurements and to
    have the high voltage power supply at 0 V when opening the sample chamber.

26. When finished with the experiment, turn the laser “rate” knob to the off
    position and then turn the key to the off position. Make sure all knobs
    on the power supply are set to 0 and turn the “high voltage” switch to
    off. Finally, turn the ``power`` switch of the power supply to off.

27. Close the TekScope program and have your TA eject the flash drive so you
    can retrieve your data. Turn the oscilloscope off.

28. Obtain 1 UV-VIS spectrum per sample and 1 fluorometer spectrum just for
    the sample with no quencher, for a total of 6 more graphs. The instructions
    for these instruments are next to them in the lab.

Results and Discussion
======================

Calculations
------------

Time-resolved fit
~~~~~~~~~~~~~~~~~

From the time-resolved fluorescence decay data, remove the points preceding
the excitation and laser pulse. The objective is to have a single exponential
decay profile.

With the cleaned data, use a non-linear regression algorithm to fit the
following function:

.. math::

    I(t) = I(0) e^{-k \cdot t}

The independent variable is time, t, the dependent variable is the intensity
at this time, I(t), and the two fit parameters are the initial intensity, I(0),
and the decay rate, k.

.. math::

    y = p_0 * exp(-p_1 * x)

Report the fit initial intensities, I(0), and decay rates, k, for all of your
decay profiles and report their fit error bars and the :math:`\chi^2_{red}` of
the fit.

Explain whether quinine is a dynamic quencher or a static quencher.

The literature value for the lifetime, :math:`\tau = k_f^{-1} = 19.3 \pm 0.6 ns`
(95% confidence limits) [Barrow]_. Compare this with your results and discuss
any discrepancies.

.. admonition:: Example exponential plot and fits
    :class: note

    The following is an example time-resolved fluorescence decay profile with
    the extra points before the fluorescence begins (before truncation) and the
    profile with these extra points removed (after truncation).

    .. plot:: experiments/lif/figures/exp_fit/exp_fit.py

Quencher rate fit
~~~~~~~~~~~~~~~~~

Plot the apparent quencher concentration, [Q], as a function of the
fluorescence decay rates, k\ :sub:`app`, concentrations of the quencher.
Describe whether
:math:`\ce{Cl-}` behaves like a dynamic quencher (equation
:eq:`fluoro-dynamic-rate-constant`) or a static quencher (equation
:eq:`fluoro-static-rate-constant`). Report the rates or equilibrium constants,
and their associated errors.

The best available literature value of :math:`k_Q = 6.2 \cdot 10^9 M^{-1}s^{-1}`
determined from lifetime measurements by Barrow and Lentz [Barrow]_. This was
determined in 0.05 M H2SO4 whereas you obtained your data in 0.5 M H2SO4.
The viscosity of 0.05 M H2SO4 is very close to that of pure water
(not the same as 0.5 M). Use the equation :eq:`diffusion-controlled` for the
diffusion-controlled rate, :math:`k_D` to quantitatively compare your results
with these and discuss any discrepancies.

.. admonition:: Example apparent rate fits with quencher concentration
    :class: note

    The following is an example plot of the quencher concentration, [Q],
    and the apparent fluorescence decay rate, k\ :sub:`app`, for dynamic
    quencher and a static quencher.

    .. plot:: experiments/lif/figures/quencher_fit/quencher_fit.py

    The fit rates are :math:`k' = (1.00000 \pm 0.000004) \cdot 10^7 s^{-1}` and
    :math:`k_Q = (9.9 \pm 0.2)  \cdot 10^4 s^{-1} M^{-1}` for the dynamic quencher and
    :math:`k' = (1.00000 \pm 0.000004) \cdot 10^7 s^{-1}` for the static quencher.
    The reported error estimates are 1 standard deviation (s.d.).

Stern-Volmer fit
~~~~~~~~~~~~~~~~

The Stern-Volmer equation :eq:`stern-volmer` relates the concentration of
excited fluorophore, [F\ :sup:`*`], to the concentration of the quencher.
We do not know these concentrations, but we do know that the initial intensity
of fluorescence, I(0), is directly proportional to [F\ :sup:`*`]--e.g. when
you double [F\ :sup:`*`], the initial fluorescent intensity, I(0), doubles, and
when there is no excited fluorophore, [F\ :sup:`*`] = 0, the initial fluorescent
intensity is also zero, I(0) = 0.

.. math::

    I(0) = C [F^*]

Where the factor C is a simple scaling constant.

The Stern-Volmer equation can be recast in terms of the initial fluorescent
intensity.

.. math::

    \frac{\{I(0)\}_0}{\{I(0)\}_Q} = \frac{[F^*]_{0}}{[F^*]} = 1 + K [Q]

Where :math:`\{I(0)\}_0` is the initial fluorescence intensity at the quencher
concentration of 0 mM, and :math:`\{I(0)\}_Q` is the initial fluorescence
intensity at the quencher concentration of [Q]. The constant 'K' is
:math:`k_q \tau` for a dynamic quencher and :math:`K_{eq}` for a static
quencher.

Collect the initial fluorescence intensities, I(0), from the mono-exponential
fits. For each concentration of the quencher, calculate the mean value and the
mean error. Plot the quencher concentration, [Q], as a function of
:math:`\{I(0)\}_0 / \{I(0)\}_Q`. Fit the plot to a linear regression and report
the associated errors on the slope and intercept. The intercept should be
close to 1.0.

.. admonition:: Example Stern-Volmer fit of initial fluorescence intensities
    :class: note

    The following is an example Stern-Volmer plot  initial fluorescence
    intensities from time-resolved fluorescence experiments.

    .. plot:: experiments/lif/figures/stern_volmer_fit/stern_volmer_fit.py


Questions
---------

#.  Using the absorbance and fluorescence spectra of quinine sulfate below
    (see :numref:`quinine-spectra`), explain why the fluorescence emission
    shows up to the *right* of the absorbance in the spectrum.

#.  Using the absorbance and fluorescence spectra of quinine sulfate below
    (see :numref:`quinine-spectra`), explain why the experiment was performed
    with a 337.1 nm laser and the fluorescence was detected at 489 nm.

#.  The absorbance spectra of atoms in atomic absorption spectroscopy show
    sharp lines with widths of a fraction of a nanometer. Explain why the
    width of the absorption spectrum of quinine sulfate below is much larger
    (see :numref:`quinine-spectra`, below).

#.  At ~390-400 nm in the absorbance and fluorescence spectra of quinine
    sulfate, there is fluorescence emission at a *smaller* wavelength than
    in the absorbance spectrum. Why? (see :numref:`quinine-spectra`, below)



#.  For fluorescence emission and absorbance processes, we wrote the kinetic
    equations using *irreversible* reactions--i.e. one-sided arrows. Why are
    these irreversible processes?

.. _quinine-spectra:

.. figure:: figures/quinine_absorbance_fluorescence/quinine_absorbance_fluorescence.png
    :alt: Quinine sulfate absorbance and fluorescence spectra

    The absorbance and fluorescence spectra of quinine sulfate.



References
==========

.. [JPhotochem1990] Pant, D.; Tripathi, U. C.; Joshi, G. C.; Tripathi, H. B.; Pant, D. D. J. Photochem. Photobio. A 1990, 51, 313-325.
.. [Harris] Harris, Daniel C., and Michael D. Bertolucci. Symmetry and Spectroscopy: An Introduction to Vibrational and Electronic Spectroscopy. New edition. New York, NY: Dover Publications, 1989.
.. [Lakowicz] Lakowicz, Joseph R., ed. “Quenching of Fluorescence.” In Principles of Fluorescence Spectroscopy, 277–330. Boston, MA: Springer US, 2006. https://doi.org/10.1007/978-0-387-46312-4_8.
.. [Gutow] Gutow, J. H.; Zare, R. N. J. Phys. Chem. 1992, 96, 2534-2543.
.. [PhysicalChemistry] Engel, Thomas, and Philip Reid. Physical Chemistry. 3rd edition. Boston: Pearson, 2012.
.. [Barrow] Barrow, David A., and Barry R. Lentz. “Quinine as a Fluorescence Lifetime Standard: Conditions for Effectively Homogeneous Decay.” Chemical Physics Letters 104, no. 2 (February 3, 1984): 163–67. https://doi.org/10.1016/0009-2614(84)80189-X.

.. |H2O| replace:: H\ :sub:`2`\ O
.. |ddH2O| replace:: ddH\ :sub:`2`\ O
.. |H2SO4| replace:: H\ :sub:`2`\ SO\ :sub:`4`

