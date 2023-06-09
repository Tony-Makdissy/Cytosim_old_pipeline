% a set of beads

set simul system
{
    steric = 1, 100
    time_step = 0.001
    viscosity = 0.1
}

set space cell
{
    shape = sphere
}
[[ radius = range(2,5) ]]
new cell
{
    radius = [[ radius ]]
}

set hand kinesin
{
    binding_rate = 10
    binding_range = 0.02
    unbinding_rate = 2
    unbinding_force = 3
    display = ( color=blue; size=10; )
}

set single grafted
{
    hand = kinesin
    stiffness = 100
}

set bead particle
{
    confine = inside, 1000
    steric = 1
    display = ( coloring=1; style=7; back_color=dark_gray )
}

[[ small_particles = range(30,35) ]]

new [[small_particles]] particle
{
    radius = 0.05
    attach = grafted
}

new 16 particle
{
    radius = 0.1
    attach = grafted
}

new 4 particle
{
    radius = 0.25
}

set solid balls
{
    confine = inside, 1000
    steric = 1
    display = ( coloring=1; style=7; )
}

[[ balls = [2] ]]
%you always have two balls, right?
new [[ balls ]] balls
{
    point1 = center, 0.5
    point2 = 64, equator 0.5
}

run system
{
    nb_steps = 5000
    nb_frames = 10
}
