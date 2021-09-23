from header_particle_systems import *
#psf_always_emit         = 0x0000000002
#psf_global_emit_dir     = 0x0000000010
#psf_emit_at_water_level = 0x0000000020
#psf_billboard_2d        = 0x0000000100 # up_vec = dir, front rotated towards camera
#psf_billboard_3d        = 0x0000000200 # front_vec point to camera.
#psf_turn_to_velocity    = 0x0000000400
#psf_randomize_rotation  = 0x0000001000
#psf_randomize_size      = 0x0000002000
#psf_2d_turbulance       = 0x0000010000

####################################################################################################################
#   Each particle system contains the following fields:
#  
#  1) Particle system id (string): used for referencing particle systems in other files.
#     The prefix psys_ is automatically added before each particle system id.
#  2) Particle system flags (int). See header_particle_systems.py for a list of available flags
#  3) mesh-name.
####
#  4) Num particles per second:    Number of particles emitted per second.
#  5) Particle Life:    Each particle lives this long (in seconds).
#  6) Damping:          How much particle's speed is lost due to friction.
#  7) Gravity strength: Effect of gravity. (Negative values make the particles float upwards.)
#  8) Turbulance size:  Size of random turbulance (in meters)
#  9) Turbulance strength: How much a particle is affected by turbulance.
####
# 10,11) Alpha keys :    Each attribute is controlled by two keys and 
# 12,13) Red keys   :    each key has two fields: (time, magnitude)
# 14,15) Green keys :    For example scale key (0.3,0.6) means 
# 16,17) Blue keys  :    scale of each particle will be 0.6 at the
# 18,19) Scale keys :    time 0.3 (where time=0 means creation and time=1 means end of the particle)
#
# The magnitudes are interpolated in between the two keys and remain constant beyond the keys.
# Except the alpha always starts from 0 at time 0.
####
# 20) Emit Box Size :   The dimension of the box particles are emitted from.
# 21) Emit velocity :   Particles are initially shot with this velocity.
# 22) Emit dir randomness
# 23) Particle rotation speed: Particles start to rotate with this (angular) speed (degrees per second).
# 24) Particle rotation damping: How quickly particles stop their rotation
####################################################################################################################

particle_systems = [
  
    ("game_rain", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "prtcl_rain",
     500, 0.5, 0.33, 1.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (1.0, 0.3), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 1.0),   (1.0, 1.0),   #scale keys
     (8.2, 8.2, 0.2),           #emit box size
     (0, 0, -10.0),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),
    ("game_snow", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_snow_fall_1",
     150, 2, 0.2, 0.1, 30, 20,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 1),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 1.0),   (1.0, 1.0),   #scale keys
     (10, 10, 0.5),           #emit box size
     (0, 0, -5.0),               #emit velocity
     1,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),
    
##    ("game_blood", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a",
##     50, 0.65, 0.95, 1.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##     (0.3, 0.3), (1, 0.2),        #alpha keys
##     (1.0, 0.4), (1, 0.05),      #red keys
##     (1.0, 0.05),(1, 0.05),      #green keys
##     (1.0, 0.05),(1, 0.05),      #blue keys
##     (0.3, 0.5),   (1.0, 2.5),   #scale keys
##     (0.04, 0.01, 0.01),           #emit box size
##     (0, 1, 0.0),               #emit velocity
##     0.05,                       #emit dir randomness
##     0,                       #rotation speed
##     0.5                        #rotation damping
##    ),
##    
    ("game_blood", psf_billboard_3d |psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_1",
     500, 0.65, 3, 0.5, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.7), (0.7, 0.7),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.7), (1, 0.7),       #green keys
     (0.1, 0.7), (1, 0.7),      #blue keys
     (0.0, 0.015),   (1, 0.018),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0, 1.0, 0.3),                #emit velocity
     0.9,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),
    ("game_blood_2", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",
     2000, 0.6, 3, 0.3, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.25), (0.7, 0.1),        #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.7), (1, 0.7),       #green keys
     (0.1, 0.7), (1, 0.7),      #blue keys
     (0.0, 0.15),   (1, 0.35),    #scale keys
     (0.01, 0.2, 0.01),             #emit box size
     (0.2, 0.3, 0),                 #emit velocity
     0.3,                         #emit dir randomness
     150,                       #rotation speed
     0,                       #rotation damping
     ),
    
 #   ("game_hoof_dust", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a",
 #    50, 1.0, 0.95, -0.1, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
 #    (0.0, 0.5), (1, 0.0),        #alpha keys
 #    (1.0, 0.9), (1, 0.05),      #red keys
 #    (1.0, 0.8),(1, 0.05),      #green keys
 #    (1.0, 0.7),(1, 0.05),      #blue keys
 #    (0.0, 7.5),   (1.0, 15.5),   #scale keys
 #    (0.2, 0.3, 0.2),           #emit box size
 #    (0, 0, 2.5),               #emit velocity
 #    0.05,                       #emit dir randomness
 #    100,                       #rotation speed
 #    0.5                        #rotation damping
 #   ),
     ("game_hoof_dust", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     5, 2.0,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.5), (1, 0.0),        #alpha keys
     (0, 1), (1, 1),        #red keys
     (0, 0.9),(1, 0.9),         #green keys
     (0, 0.78),(1, 0.78),         #blue keys
     (0.0, 2.0),   (1.0, 3.5),   #scale keys
     (0.2, 0.3, 0.2),           #emit box size
     (0, 0, 3.9),                 #emit velocity
     0.5,                         #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("game_hoof_dust_snow", psf_billboard_3d|psf_randomize_size, "prt_mesh_snow_dust_1",#prt_mesh_dust_1
     6, 2, 3.5, 1, 10.0, 0.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 1),        #alpha keys
     (0, 1), (1, 1),        #red keys
     (0, 1),(1, 1),         #green keys
     (0, 1),(1, 1),         #blue keys
     (0.5, 4),   (1.0, 5.7),   #scale keys
     (0.2, 1, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),
     ("game_hoof_dust_mud", psf_billboard_2d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_mud_1",#prt_mesh_dust_1
     5, .7,  10, 3, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, .7), (1, .7),        #red keys
     (0, 0.6),(1, 0.6),         #green keys
     (0, 0.4),(1, 0.4),         #blue keys
     (0.0, 0.2),   (1.0, 0.22),   #scale keys
     (0.15, 0.5, 0.1),           #emit box size
     (0, 0, 15),                 #emit velocity
     6,                         #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("game_water_splash_1", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_emit_at_water_level, "prtcl_drop",
     20, 0.85, 0.25, 0.9, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 0.5), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 0.3),   (1.0, 0.18),   #scale keys
     (0.3, 0.2, 0.1),           #emit box size
     (0, 1.2, 2.3),               #emit velocity
     0.3,                       #emit dir randomness
     50,                       #rotation speed
     0.5                        #rotation damping
    ),
    
    ("game_water_splash_2", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_emit_at_water_level, "prtcl_splash_b",
     30, 0.4, 0.7, 0.5, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 0.25),   (1.0, 0.7),   #scale keys
     (0.4, 0.3, 0.1),           #emit box size
     (0, 1.3, 1.1),               #emit velocity
     0.1,                       #emit dir randomness
     50,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("game_water_splash_3", psf_emit_at_water_level , "prt_mesh_water_wave_1",
     5, 2.0, 0, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.03, 0.2), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 3),   (1.0, 10),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("torch_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 0.35, 0.2, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.04, 0.04, 0.01),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),
    ("fire_glow_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_fire_2",
     2, 0.55, 0.2, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.9), (1, 0),          #alpha keys
     (0.0, 0.9), (1, 0.9),      #red keys
     (0.0, 0.7),(1, 0.7),       #green keys
     (0.0, 0.4), (1, 0.4),      #blue keys
     (0, 2),   (1.0, 2),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

    ("fire_glow_fixed", psf_billboard_3d|psf_global_emit_dir, "prt_mesh_fire_2",
     4, 100.0, 0.2, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (-0.01, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0.9), (1, 0.9),      #red keys
     (0.0, 0.7),(1, 0.7),       #green keys
     (0.0, 0.4), (1, 0.4),      #blue keys
     (0, 2),   (1.0, 2),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

    ("torch_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prtcl_dust_a",
     15, 0.5, 0.2, -0.2, 10.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.25), (1, 0),       #alpha keys
     (0.0, 0.2), (1, 0.1),      #red keys
     (0.0, 0.2),(1, 0.09),      #green keys
     (0.0, 0.2), (1, 0.08),     #blue keys
     (0, 0.5),   (0.8, 2.5),    #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1                        #emit dir randomness
    ),
     ("flue_smoke_short", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
     15, 1.5, 0.1, -0.0, 10.0, 12, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.3), (1, 0),        #alpha keys
     (0.0, 0.2), (1, 0.1),      #red keys
     (0.0, 0.2),(1, 0.09),      #green keys
     (0.0, 0.2), (1, 0.08),     #blue keys
     (0, 1.5),   (1, 7),          #scale keys
     (0, 0, 0),           #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1,                        #emit dir randomness
     150,
     0.8,
    ),
    ("flue_smoke_tall", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
     15, 3, 0.5, -0.0, 15.0, 12,#num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.35), (1, 0),         #alpha keys
     (0.0, 0.3), (1, 0.1),      #red keys
     (0.0, 0.3),(1, 0.1),       #green keys
     (0.0, 0.3), (1, 0.1),      #blue keys
     (0, 2),   (1, 7),        #scale keys
     (0, 0, 0),                 #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1,                       #emit dir randomness
     150,
     0.5,
    ),

    ("war_smoke_tall", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
     5, 12, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 2.2),   (1, 15),        #scale keys
     (0, 0, 0),                 #emit box size
     (0, 0, 2.2),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),
    
     ("ladder_dust_6m", psf_billboard_3d, "prt_mesh_smoke_1",
     700, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 3.5),                 #emit box size  (6.5 is equal to (12m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

     ("ladder_dust_8m", psf_billboard_3d, "prt_mesh_smoke_1",
     900, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 4.5),                 #emit box size  (6.5 is equal to (12m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

     ("ladder_dust_10m", psf_billboard_3d, "prt_mesh_smoke_1",
     1100, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 5.5),                 #emit box size  (6.5 is equal to (12m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

     ("ladder_dust_12m", psf_billboard_3d, "prt_mesh_smoke_1",
     1300, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 6.5),                 #emit box size  (6.5 is equal to (12m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

     ("ladder_dust_14m", psf_billboard_3d, "prt_mesh_smoke_1",
     1500, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 7.5),                 #emit box size  (7.5 is equal to (14m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

    ("ladder_straw_6m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     700, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 3.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("ladder_straw_8m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     900, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 4.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("ladder_straw_10m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     1100, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 5.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("ladder_straw_12m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     1300, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 6.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("ladder_straw_14m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     1500, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 7.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("torch_fire_sparks", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size,  "prt_sparks_mesh_1",
     10, 0.7, 0.2, 0, 10.0, 0.02,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.66, 1), (1, 0),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.1), (1, 0.1),      #blue keys
     (0.1, 0.05),   (1, 0.05),  #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 0.9),               #emit velocity
     0.0,                       #emit dir randomness
     0,
     0,
    ),

    ("fire_sparks_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size,  "prt_sparks_mesh_1",
     10, 1.5, 0.2, 0, 3, 10,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.6, 1), (1, 1),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.1), (1, 0.1),      #blue keys
     (0.1, 0.07),   (1, 0.03),    #scale keys
     (0.17, 0.17, 0.01),           #emit box size
     (0, 0, 1),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0,
    ),
    
    ("pistol_smoke", psf_billboard_3d, "prtcl_dust_a",
     90, 2.5, 0.6, -0.2, 60.0, 1.5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.75), (1, 0),       #alpha keys
     (0.0, 0.7), (1, 0.4),      #red keys
     (0.0, 0.7),(1, 0.4),       #green keys
     (0.0, 0.7), (1, 0.4),      #blue keys
     (0, 1.5),   (0.5, 11.0),   #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (2, 2, 0),                 #emit velocity
     0.1                        #emit dir randomness
    ),
    
#    ("cooking_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prtcl_fire",
#    50, 0.5, 0.2, -0.05, 30.0, 0.3,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
#    (0.5, 1), (1, 1),          #alpha keys
#     (0.5, 1.0), (1, 0.9),     #red keys
#     (0.5, 0.4), (1, 0.1),     #green keys
#     (0.5, 0.2), (1, 0.0),     #blue keys
#     (0.3, 0.9),   (0.9, 2),   #scale keys
#     (0.07, 0.07, 0.01),       #emit box size
#     (0, 0, 0.1),              #emit velocity
#     0.1                       #emit dir randomness
#    ),

     ("brazier_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.5, 0.1, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.4), (1.0, 0),        #alpha keys
     (0.5, 1.0), (1.0, 0.9),      #red keys
     (0.5, 0.7),(1.0, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.1, 0.2),   (1.0, 0.5),      #scale keys
     (0.1, 0.1, 0.01),        #emit box size
     (0.0, 0.0, 0.4),                 #emit velocity
     0.0,                       #emit dir randomness
     100,                       #rotation speed
     0.2                        #rotation damping
     ),
#              ("cooking_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_steam_1",
#     3, 3.5, 0.4, -0.03, 10.0, 10.9,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
#     (0.4, 1), (1, 0),          #alpha keys
 #    (0.0, 0.6), (1, 0.3),      #red keys
#     (0.0, 0.6),(1, 0.3),       #green keys
#     (0.0, 0.6), (1, 0.3),      #blue keys
#     (0, 2.5),   (0.9, 7.5),    #scale keys
 #    (0.1, 0.1, 0.06),          #emit box size
 #    (0, 0, 1.3),               #emit velocity
#     0.2,                       #emit dir randomness
 #    200,                       #rotation speed
 #    0.2,                       #rotation damping
 #   ),

    ("cooking_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.35, 0.1, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 0.5*1.0), (1, 0.3*0.9),      #red keys
     (0.5, 0.5*0.7),(1, 0.3*0.3),       #green keys
     (0.5, 0.5*0.2), (1, 0.0),      #blue keys
     (0.1, 0.5),   (1, 1),      #scale keys
     (0.05, 0.05, 0.01),        #emit box size
     (0, 0, 1),                 #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.0                        #rotation damping
     ),
    
    ("cooking_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
     4, 4, 0.1, 0, 3, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.20), (1.0, 0.0),          #alpha keys
     (0.0, 0.8), (1.0, 1.0),      #red keys
     (0.0, 0.8),(1.0, 1.0),      #green keys
     (0.0, 0.85), (1.0, 1.0),     #blue keys
     (0.0, 0.65),   (1.0, 3.0),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 1.2),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0,
    ),

    ("food_steam", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_steam_1",
     3, 1, 0, 0, 8.0, 1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.1), (1, 0),        #alpha keys
     (0.0, 1), (1, 0.1),        #red keys
     (0.0, 1),(1, 0.1),         #green keys
     (0.0, 1), (1, 0.1),        #blue keys
     (0, 0.2),   (0.9, 0.5),      #scale keys
     (0.05, 0.05, 0),          #emit box size
     (0, 0, 0.1),               #emit velocity
     0,                         #emit dir randomness
     100,                       #rotation speed
     0.5,                       #rotation damping
    ),

    ("candle_light", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_candle_fire_1",
     7, 1.1, 0.6, -0.0, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.3, 0.2),   (1, 0.0),    #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0.09),              #emit velocity
      0,                        #emit dir randomness
      0,                        #rotation speed
      0                         #rotation damping
    ),
    ("candle_light_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_candle_fire_1",
     4, 1.1, 0.6, -0.0, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.3, 0.13),   (1, 0.0),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0.06),              #emit velocity
      0,                        #emit dir randomness
      0,                        #rotation speed
      0                         #rotation damping
    ),
    ("lamp_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
     10, 0.8, 0.6, -0.0, 10.0, 0.4,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.8), (1, 0.1),      #green keys
     (0.5, 0.4), (1, 0.0),      #blue keys
     (0.3, 0.35), (0.9, 0.5),    #scale keys
     (0.01, 0.01, 0.0),         #emit box size
     (0, 0, 0.35),               #emit velocity
     0.03,                      #emit dir randomness
     100,                       #rotation speed
     0.5,                       #rotation damping
    ),
#*-*-*-*-* D U M M Y *-*-*-*-#
    ("dummy_smoke", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 3, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 0.7),   (1, 2.2),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("dummy_straw", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     500, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("dummy_smoke_big", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 9, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.9), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 5),   (1, 15.0),    #scale keys
     (3, 3, 5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("dummy_straw_big", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     500, 3, 2, 2.0, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.8),   (1, 0.8),    #scale keys
     (3, 3, 3),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

#*-*-*-*-* D U M M Y  E N D *-*-*-*-#
#*-*-*-*-* GOURD *-*-*-*-#
    ("gourd_smoke", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 3, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 0.5),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("gourd_piece_1", psf_randomize_rotation,  "prt_gourd_piece_1",
     15, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    
    ("gourd_piece_2", psf_randomize_size | psf_randomize_rotation,  "prt_gourd_piece_2",
     50, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    
##    ("rat_particle", psf_global_emit_dir|psf_2d_turbulance | psf_randomize_size |psf_billboard_3d,  "rat_particle",
##     500, 4, 0, 0, 20, 10,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##     (0.1, 1), (1, 1),          #alpha keys
##     (0.1, 0.6), (1, 0.6),      #red keys
##     (0.1, 0.5),(1, 0.5),       #green keys
##     (0.1, 0.4), (1, 0.4),      #blue keys
##     (0.1, 1),   (1, 1),        #scale keys
##     (0.1, 0.1, 0.1),           #emit box size
##     (0, 0, 0),                 #emit velocity
##     5,                         #emit dir randomness
##    ),

#*-*-*-**** BLOOD ****-*-*-*#
    
##("blood_hit_1", psf_billboard_3d | psf_randomize_size ,  "prt_mesh_blood_1",
##     5000, 0.5, 6, 0.5, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##     (0.1, 1), (1, 0),          #alpha keys
##     (0.1, 0.6), (1, 0.6),      #red keys
##     (0.1, 0.5),(1, 0.5),       #green keys
##     (0.1, 0.4), (1, 0.4),      #blue keys
##     (0.0, 0.05),   (1, 0.05),  #scale keys
##     (0, 0.5, 0),               #emit box size
##     (0, -1, 0),                #emit velocity
##     1.5,                       #emit dir randomness
##     0,                         #rotation speed
##     0,                         #rotation damping
##    ),
##    #("blood_hit_2", 0 ,  "prt_mesh_blood_2",
##    # 500, 0.3, 0,0, 0, 0,       #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##    # (0.1, 1), (1, 0.0),        #alpha keys
##    # (0.1, 0.6), (1, 0.6),      #red keys
##    # (0.1, 0.5),(1, 0.5),       #green keys
##    # (0.1, 0.4), (1, 0.4),      #blue keys
##    # (0.0, 0.4),   (1, 2),      #scale keys
##    # (0.0, 0.0, 0.0),           #emit box size
##    # (0, -0.1, 0),              #emit velocity
##    # 0,                         #emit dir randomness
##    # 0,                         #rotation speed
##    # 0,                         #rotation damping
##    # ),
##    ("blood_hit_3", psf_billboard_3d | psf_randomize_size ,  "prt_mesh_blood_3",
##     500, 0.3, 1,0.0, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##     (0.1, 1), (1, 0.0),        #alpha keys
##     (0.1, 0.6), (1, 0.6),      #red keys
##     (0.1, 0.5),(1, 0.5),       #green keys
##     (0.1, 0.4), (1, 0.4),      #blue keys
##     (0.0, 0.2),   (1, 0.8),    #scale keys
##     (0.0, 0.3, 0.0),           #emit box size
##     (0, 1, 0),                 #emit velocity
##     1,                         #emit dir randomness
##     250,                       #rotation speed
##     0,                       #rotation damping
##     ),
    
#*-*-*-**** BLOOD  END ****-*-*-*#

#-*-*-*- Fire Fly Deneme *-*-*-*-#    
     ("fire_fly_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_sparks_mesh_1",
     2, 5, 1.2, 0, 50, 7,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0.2),        #alpha keys
     (0.5, .7), (1, 0.7),      #red keys
     (0.5, 0.8), (1, 0.8),      #green keys
     (0.5, 1), (1, 1),      #blue keys
     (0, 0.1),   (1, 0.1),    #scale keys
     (20, 20, 0.5),             #emit box size
     (0, 0, 0),              #emit velocity
      5,                        #emit dir randomness
      0,                        #rotation speed
      0                         #rotation damping
       ),
     ("bug_fly_1", psf_billboard_2d | psf_always_emit, "prt_mesh_rose_a",
     20, 8, 0.02, 0.025, 1, 5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (10, 5, 0.1),             #emit box size
     (0, 0, -0.9),              #emit velocity
      0.01,                        #emit dir randomness
      10,                        #rotation speed
      0,                         #rotation damping
    ),
#-*-*-*- Fire Fly End*-*-*-*-#
#-*-*-*- Moon Beam *-*-*-*-*-*-*#
    ("moon_beam_1", psf_billboard_2d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_mesh_moon_beam",#prt_mesh_moon_beam
     2, 4, 1.2, 0, 0, 0,          #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 1), (1, 0),            #alpha keys
     (0, 0.4), (1, 0.4),                #red keys
     (0, 0.5), (1, 0.5),                #green keys
     (0, 0.6), (1, 0.6),                #blue keys
     (0, 2),   (1, 2.2),        #scale keys
     (1, 1, 0.2),                 #emit box size
     (0, 0, -2),                     #emit velocity
      0,                            #emit dir randomness
      100,                          #rotation speed
      0.5,                          #rotation damping
       ),
     ("moon_beam_paricle_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_sparks_mesh_1",
     10, 1.5, 1.5, 0, 10, 10,            #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 1), (1, 0.0),            #alpha keys
     (0.5, .5), (1, 0.5),           #red keys
     (0.5, 0.7), (1, 0.7),          #green keys
     (0.5, 1), (1, 1),              #blue keys
     (0, 0.1),   (1, 0.1),        #scale keys
     (1, 1, 4),                 #emit box size
     (0, 0, 0),                     #emit velocity
      0.5,                            #emit dir randomness
      0,                            #rotation speed
      0                             #rotation damping
       ),
#-*-*-*- Moon Beam End *-*-*-*-*-*-*#
#-*-*-*- Stone Smoke *-*-*-*-*-*-*#
##("stone_hit_1", psf_billboard_3d | psf_randomize_size | psf_randomize_rotation,  "prt_mesh_dust_1",
##     5000, 0.5, 6, 0.1, 0, 0,       #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##     (0.1, .2), (1, 0),             #alpha keys
##     (0.5, 0.7), (1, 0.7),          #red keys
##     (0.5, 0.6), (1, 0.6),          #green keys
##     (0.5, 0.6), (1, 0.6),          #blue keys
##     (0.0, .2),   (1, 0.7),         #scale keys
##     (0, 0.3, 0),                   #emit box size
##     (0, 0, 0),                     #emit velocity
##     1.1,                           #emit dir randomness
##     200,                           #rotation speed
##     0.8,                           #rotation damping
##    ),
#-*-*-*- Stone Smoke END -*-*-*-*-*#
    ("night_smoke_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_dust_1",
     5, 10, 1.5, 0, 50, 2,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 0.1), (1, 0),        #alpha keys
     (0.5, 0.5), (1, 0.5),      #red keys
     (0.5, 0.5), (1, 0.5),      #green keys
     (0.5, 0.5), (1, 0.6),      #blue keys
     (0, 10),   (1, 10),        #scale keys
     (25, 25, 0.5),               #emit box size
     (0, 1, 0),                 #emit velocity
      2,                        #emit dir randomness
      20,                       #rotation speed
      1                         #rotation damping
       ),
#-*-*-*- Fire For Fireplace -*-*-*-#
    ("fireplace_fire_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.8, 0.2, -0.1, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.2),   (1, 0.7),   #scale keys
     (0.2, 0.1, 0.01),      #emit box size
     (0, 0, 0.2),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5                        #rotation damping
    ),
    ("fireplace_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     35, 0.6, 0.2, -0.2, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.4),   (1, 1),   #scale keys
     (0.4, 0.2, 0.01),            #emit box size
     (0, 0, 0.4),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5                        #rotation damping
    ),  
#-*-*-*- Fire For Fireplace -*-*-*-#
#-*-*-*- Village Fire *-*-*-*-#
    ("village_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 1.0, 0, -1.2, 25.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.7), (1, 0),        #alpha keys
     (0.2, 1.0), (1, 0.9),      #red keys
     (0.2, 0.7),(1, 0.3),       #green keys
     (0.2, 0.2), (1, 0.0),      #blue keys
     (0, 2),   (1, 6),          #scale keys
     (2.2, 2.2, 0.2),           #emit box size
     (0, 0, 0.0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),
    ("village_fire_smoke_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     30, 2, 0.3, -1, 50.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),        #alpha keys
     (0.2, 0.4), (1, 0.2),      #red keys
     (0.2, 0.4),(1, 0.2),       #green keys
     (0.2, 0.4), (1, 0.2),      #blue keys
     (0, 6),   (1, 8),          #scale keys
     (2, 2, 1),           #emit box size
     (0, 0, 5),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.1                        #rotation damping
    ), 
    ("map_village_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     20, 1.0, 0, -0.2, 3.0, 3.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.7), (1, 0),        #alpha keys
     (0.2, 1.0), (1, 0.9),      #red keys
     (0.2, 0.7),(1, 0.3),       #green keys
     (0.2, 0.2), (1, 0.0),      #blue keys
     (0, 0.15),   (1, 0.45),    #scale keys
     (0.2, 0.2, 0.02),           #emit box size
     (0, 0, 0.0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),
    ("map_village_fire_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     25, 2.5, 0.3, -0.15, 3.0, 3.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),       #alpha keys
     (0.2, 0.4), (1, 0.3),      #red keys
     (0.2, 0.4),(1, 0.3),       #green keys
     (0.2, 0.4), (1, 0.3),      #blue keys
     (0, 0.6),   (1, 0.9),      #scale keys
     (0.2, 0.2, 0.1),           #emit box size
     (0, 0, 0.03),              #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0.1                        #rotation damping
    ), 
    ("map_village_looted_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     20, 3, 0.3, -0.11, 3.0, 2.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),       #alpha keys
     (0.2, 0.5), (1, 0.5),      #red keys
     (0.2, 0.5),(1, 0.5),       #green keys
     (0.2, 0.5), (1, 0.5),      #blue keys
     (0, 0.7),   (1, 1.3),      #scale keys
     (0.2, 0.2, 0.1),           #emit box size
     (0, 0, 0.015),             #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0.1                        #rotation damping
    ), 
##### Dungeon Water Drops #####
    ("dungeon_water_drops", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "prtcl_rain",
     1, 1, 0.33, 0.8, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (1.0, 0.2), (1, 0.2),      #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 0.8),   (1.0, 0.8),  #scale keys
     (0.05, 0.05, 0.5),         #emit box size
     (0, 0, -5.0),              #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
     ), 
##### Dungeon Water Drops  END #####
    ("wedding_rose", psf_billboard_2d | psf_always_emit, "prt_mesh_rose_a",
     50, 8, 0.02, 0.025, 1, 5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (4, 4, 0.1),             #emit box size
     (0, 0, -0.9),              #emit velocity
      0.01,                        #emit dir randomness
      10,                        #rotation speed
      0,                         #rotation damping
    ),
    ("sea_foam_a", psf_turn_to_velocity | psf_always_emit|psf_randomize_size, "prt_foam_a",
     1, 3.0, 1, 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.7, 0.1), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 4),   (1.0, 4.5),   #scale keys
     (10.0, 1.0, 0),           #emit box size
     (0, 1, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),
    ("fall_leafs_a", psf_billboard_2d | psf_always_emit, "prt_mesh_yrellow_leaf_a",
     1, 9, 0, 0.025, 4, 4,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),            #alpha keys
     (0, 0.5), (1, 0.5),        #red keys
     (0, 0.5), (1, 0.5),        #green keys
     (0, 0.5), (1, 0.5),        #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (4, 4, 4),                 #emit box size
     (0, 0.01, -0.9),           #emit velocity
      0.02,                     #emit dir randomness
      15,                       #rotation speed
      0,                        #rotation damping
    ),
  
    ("bullet_hit", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation| psf_global_emit_dir, "prtcl_dust_a",
      500, 3, 8, 0.2, 2, 20, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
      (0.0, 0.6), (1, 0),     #alpha keys
      (0.0, 0.95), (1, 0.95),          #red keys
      (0.0, 0.90), (1, 0.90),           #green keys
      (0.0, 0.70), (1, 0.70),          #blue keys
      (0, 3), (1.6, 4),  #scale keys
      (0, 0, 0),         #emit box size
      (0, 0, 10),               #emit velocity
      3,                      #emit dir randomness
      100,                     #rotation speed
      0.2                       #rotation damping
    ),
    ("musket_flash", psf_billboard_3d | psf_randomize_size , "prt_sparks_mesh_1",
     3000, 0.5, 0.1, -0.00003, 50.0, 1.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.0, 0.9),   (0.75, 0.1),   #scale keys
     (0.1, 0.2, 0.1),           #emit box size
     (0.4, 2.2, 0.4),                 #emit velocity
     0.05,                       #emit dir randomness
     100.0,                       #rotation speed
     0.5,                        #rotation damping
    ),
    ("musket_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "smoke_white1", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
     75, 22, 2, -0.006040, 90, 3.3,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.3), (0.349, 0),       #alpha keys
     (0.0, 0.99), (1, 0.99),      #red keys
     (0.0, 0.99),(1, 0.99),       #green keys
     (0.0, 0.99), (1, 0.99),      #blue keys
     (-0.01, 3.45),   (0.5, 12.7),   #scale keys
     (0.05, 0.05, 0.05),           #emit box size
     (0.0, 5.6, 0.0),                 #emit velocity
     0.85,                        #emit dir randomness
     90,                       #rotation speed
     0.25,                        #rotation damping
    ),
   ("pan_flash", psf_billboard_3d | psf_randomize_size , "prt_sparks_mesh_1",
     3000, 0.3, 0.1, -0.00003, 50.0, 1.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.0, 0.8),   (0.6, 0.6),   #scale keys
     (0.1, 0.1, 0.6),           #emit box size
     (0, 0, 0.6),                 #emit velocity
     0.05,                       #emit dir randomness
     100.0,                       #rotation speed
     0.5,                        #rotation damping
    ),
   ("pan_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
     60, 10.6, 1.8, -0.0003, 90, 4,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.55), (0.549, 0),       #alpha keys
     (0.0, 0.99), (1, 0.99),      #red keys
     (0.0, 0.99),(1, 0.99),       #green keys
     (0.0, 0.99), (1, 0.99),      #blue keys
     (-0.07, 1.5),   (0.5, 3.75),   #scale keys
     (0.02, 0.02, 0.02),           #emit box size
     (-1.6, 0.6, 0.0),                 #emit velocity
     0.0,                        #emit dir randomness                       
    ),
  ("musket_sparks", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size,  "prt_sparks_mesh_1",
     10, 0.7, 0.2, 0, 10.0, 0.02,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.1, 0.05),   (1, 0.05),  #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 0.9),               #emit velocity
     0.0,                       #emit dir randomness
     0,
     0,
    ),
    ("cannon_smoke", psf_billboard_3d, "smoke_white1",
     10000, 12, 1.14, -0.015, 40, 1.75,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.4), (0.65, 0),       #alpha keys
     (0.0, 0.9), (1, 0.9),      #red keys
     (0.0, 0.9),(1, 0.9),       #green keys
     (0.0, 0.99), (1, 0.99),      #blue keys
     (-0.1, 6),   (1.0, 17.0),   #scale keys
     (0.3, 0.3, 0.3),           #emit box size
     (2, 7, 0),                 #emit velocity
     2.3,                        #emit dir randomness
     90,                       #rotation speed
     0.4,                        #rotation damping
    ),
    ("cannon_ball_hit", psf_billboard_3d|psf_always_emit|psf_randomize_size,  "YuriCannonballHitGroundDirt",
     2000, 2, 15, -0.65, 12.0, 0.4,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (6.0, 6.7),   (7, 8.2),    #scale keys
     (0.45, 0.46, 3.2),         #emit box size
     (0, 0, 0.1),               #emit velocity
     4,                         #emit dir randomness
     15,                        #rotation speed
     0.1,                       #rotation damping
    ),
  ("explosion_smoke_white1", psf_billboard_3d|psf_billboard_drop, "smoke_white1",
    1000, 4.25, 2, -0.01, 40, 1.75,  #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    (0, 0.7), (1, 0),    #alpha keys
    (0, 1), (1, 1),    #red keys
    (0, 1), (1, 1),     #green keys
    (0, 1), (1, 1),    #blue keys
    (0, 7), (0.8, 30),  #scale keys
    (0, 0, 0),        #emit box size
    (3, 0, 8.5),        #emit velocity
    7                       #emit dir randomness         
  ),
  ("explosion_smoke_white2", psf_billboard_3d|psf_billboard_drop, "smoke_white1b",
    1000, 8, -0.1, -0.007, 40, 1.75,  #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    (0.4, 0.5), (1, 0),    #alpha keys
    (0, 1), (1, 1),    #red keys
    (0, 1), (1, 1),     #green keys
    (0, 1), (1, 1),    #blue keys
    (0, 12), (0.7, 34),  #scale keys
    (1, 1, 2),        #emit box size
    (2, 0, 0),        #emit velocity
    1.2                       #emit dir randomness         
  ),
    ("ground_debris1", psf_billboard_3d|psf_billboard_drop, "prt_ground_debris1",
    1000, 4, 2, 2, 10, 1,  #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    (0, 1), (1, 1),    #alpha keys
    (0, 0.5), (1, 0.5),    #red keys
    (0, 0.5), (1, 0.5),     #green keys
    (0, 0.5), (1, 0.5),    #blue keys
    (0, 1), (1, 1),  #scale keys
    (0, 0, 0),        #emit box size
    (0, 0, 5),        #emit velocity
    30                       #emit dir randomness         
  ),
  ("explosion_flash", psf_billboard_3d|psf_billboard_drop|psf_randomize_size, "flash_white1",
    3000, 2.8, 0, 0, 50, 1, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    (0.1, 0.8), (1, 0),		#alpha keys
    (0.5, 1), (1, 0.9),		#red keys
    (0.5, 0.6), (1, 0.1),		#green keys
    (0.5, 0.2), (1, 0),		#blue keys
    (0.05, 8), (0.5, 0.5),	#scale keys
    (0.2, 0.2, 1),			#emit box size
    (0, 0, 0),				#emit velocity
    0.05,					#emit dir randomness         
    100, 0.5
),
  ("musket_smoke_smokelesspowder", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
     75, 7, 2, -0.006040, 90, 3.3,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.4), (0.449, 0),       #alpha keys
     (0.0, 0.99), (1, 0.99),      #red keys
     (0.0, 0.99),(1, 0.99),       #green keys
     (0.0, 0.99), (1, 0.99),      #blue keys
     (-0.01, 2.45),   (0.5, 9),   #scale keys
     (0.05, 0.05, 0.05),           #emit box size
     (0.0, 3.6, 0.0),                 #emit velocity
     0.85,                        #emit dir randomness
     90,                       #rotation speed
     0.25,                        #rotation damping
    ),
  ("rain1", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "rain1",
     9999, 0.9, 0.33, 2.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (1.0, 0.25), (1, 0.25),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 1.0),   (1.0, 1.0),   #scale keys
     (9.2, 9.2, 0.2),           #emit box size
     (0, 0, -12.0),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),
  ("thunder1", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "thunder1",
     1.5, 1, 0, 0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 1.0),   (1.0, 1.0),   #scale keys
     (0, 0, 0),           #emit box size
     (0, 0, 0),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),
  ("thunder2", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "thunder2",
     1.5, 1, 0, 0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 1.0),   (1.0, 1.0),   #scale keys
     (0, 0, 0),           #emit box size
     (0, 0, 0),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),
  ("thunder_end", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "thunder2",
     1.5, 1, 0, 0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 1.0),   (1.0, 1.0),   #scale keys
     (0, 0, 0),           #emit box size
     (0, 0, 0),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),
  ("cartridge_case", psf_randomize_rotation, "cartridge_case", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
     100, 3, 2, 2.5, 0.1, 0.05,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 1), (1, 1),       #alpha keys
     (0.0, 1), (1, 1),      #red keys
     (0.0, 1),(1, 1),       #green keys
     (0.0, 1), (1, 1),      #blue keys
     (0, 1),   (1, 1),   #scale keys
     (0, 0, 0),           #emit box size
     (-6, 1, 0.0),                 #emit velocity
     0.1,                        #emit dir randomness
     0.1,                       #rotation speed
     1,                        #rotation damping
    ),
  ("smoke_gas", psf_billboard_2d, "smoke_gas1",
    10000, 50, 20, 0, 7, 7,  #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    (0.7, 0.5), (1, 0),    #alpha keys
    (0, 1), (1, 1),    #red keys
    (0, 1), (1, 1),     #green keys
    (0, 1), (1, 1),    #blue keys
    (0, 70), (0.5, 70),  #scale keys
    (21, 21, 5),        #emit box size
    (10, 10, 30),        #emit velocity
    20                       #emit dir randomness         
  ),
  ("smoke_gas2", psf_billboard_2d|psf_global_emit_dir, "smoke_gas2",
    14, 2.5, 0, -0.14, 0, 0,  #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    (0.5, 0.3), (1, 0),    #alpha keys
    (0, 1), (1, 1),    #red keys
    (0, 1), (1, 1),     #green keys
    (0, 1), (1, 1),    #blue keys
    (0, 0.5), (0.5, 4),  #scale keys
    (0, 0, 0),        #emit box size
    (0.1, 0, 0.1),        #emit velocity
    0.3                       #emit dir randomness         
  ),

]


# modmerger_start version=201 type=2
try:
    component_name = "particle_systems"
    var_set = { "particle_systems" : particle_systems }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
