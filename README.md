The workflow requires the GPUFLOW code (Cappello et al., 2022, https://doi.org/10.3390/app12094395).

The code is developed in 5 Python scripts:

1) input_parameters.py, which contains the values of the input parameters used to run the simulation such as coordinates of the central position of the domain where the search for potential vents will be carried out,
   time start and time end of the simulation, path to the Digital Elevation Model and real lava flow as rasters;
2) main.py, which contains the main part of the workflow;
3) create_input.files, which create the files reuqired to run the GPUFLOW code;
4) run.py, which run the GPUFLOW code and calculate the fit for each iteration
5) post-processing.py, which at the end of the workflow creates the csv file with accepted combination of parameters and makes the correlation matrix

The code may work also for multiple vents, which need proper modifications of the scripts.
