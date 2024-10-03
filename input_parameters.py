#### Input Parameters 2017 ERUPTION####
dem = "../../dem_2016_corr_10m"
reale = ["../../../lava-2017-eruption"]
fluxrate = "fluxrate-2017.txt"
emiss = 0.9

vents = {
	0: [499950, 4177470],
	}

par_vents = {
	"step_1": {
		"seq_vents":[0],
		"tstart": [0],
		"tend": [249960]
	}
}

dtsave_list = [249960]
n_samples = 200

start_step = 0
fixed_vents = False
