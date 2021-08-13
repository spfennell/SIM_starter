
trick.mc_set_enabled(1)
trick.mc_set_num_runs(5)
trick.mc_add_slave("localhost")
trick.stop(15.0);
trick.real_time_enable()
trick.sim_control_panel_set_enabled(True)