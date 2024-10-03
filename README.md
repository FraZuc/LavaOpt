The code includes 5 Python scripts:

1) input_parameters.py, which contains the values of the input parameters used to run the simulation, such as coordinates of the central position of the domain where the search for potential vents will be carried out,
   time start and time end of the simulation, path to the digital topography and reference lava flow as file rasters;
2) main.py, which contains the main part of the workflow;
3) create_input_files.py, which creates the files required to run the GPUFLOW code (Cappello et al., 2022, https://doi.org/10.3390/app12094395);
4) run.py, which runs the GPUFLOW code and calculates the fit at each iteration;
5) post-processing.py, which is run at the end of the workflow, creating the csv file with the accepted combinations of the parameters and the correlation matrix.

If properly modified, the code may work also for multiple vents.

The workflow requires the GPUFLOW code.
