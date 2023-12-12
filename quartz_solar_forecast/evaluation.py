"""
To evaluate the performance of the solar forecast, a predefined testset is used.

A file has been added to this branch (make-testset) which defines a set of random timestamps and sites ids. 
This contains 50 sites each with 50 timestamps to make 2500 samples in total.

"""

def run_eval(testset_path):
  # load testset from csv
  testset = df.read_csv(testset_path)

  # Extract generation data and metadata for specific sites and timestamps for the testset from Hugging Face.


  # Split data into PV inputs and ground truth.


  # Collect NWP data from Hugging Face, ICON.


  # Run forecast with PV and NWP inputs. 


  # Combine the forecast results with the ground truth (ts, id, horizon (in hours), pred, truth, diff)


  # Save file


  # Calculate and print metrics: MAE


  # Visulisations
