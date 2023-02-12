Create GitHub Action: Inventory


David Cannan
Necessary steps to create a github action that takes inventory of my network

Here are the steps to create a GitHub action to take inventory of your network:

Create a new GitHub repository for the action.
In the repository, navigate to the Actions tab and click on the Set up a workflow yourself button.
Create a new file named main.yml in the .github/workflows directory. This file will define your workflow.
In the main.yml file, define a new workflow that runs when the repository is pushed to. You can do this by adding the following code:
yaml
Copy code
name: Network Inventory

on:
  push:
    branches:
      - main

jobs:
  inventory:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Run inventory script
      uses: docker://image-with-inventory-script

    - name: Upload results
      uses: actions/upload-artifact@v1
      with:
        name: inventory-results
        path: path/to/inventory-results
        
        
        
In the Run inventory script step, replace image-with-inventory-script with the Docker image containing the script that you want to run.
In the Upload results step, replace path/to/inventory-results with the path to the directory containing the results of the inventory script.
Commit the changes to the main.yml file and push the repository to your GitHub account.
Wait for the workflow to run and check the Actions tab for the results of the inventory.
Note: The exact details of the inventory script will depend on what information you want to gather about your network. You may need to write this script yourself or find an existing script that you can use.




How do I run this github repo from command line on a device inside the network?

To run the GitHub repository containing your inventory script on a device inside your network, you need to clone the repository to the device and run the script. Here are the steps:

Install Git on the device if it is not already installed.
Open a terminal or command prompt window.

Clone the repository to the device by running the following command:

[shell]
$ git clone https://github.com/<your-username>/<your-repo>.git

Change into the directory containing the repository by running the following command:
shell
$ cd <your-repo>

Run the script by executing the appropriate command for your script. For example, if the script is a shell script, you could run it with the following command:
ruby
$ sh inventory-script.sh

Note: The exact command for running the script will depend on the type of script you have written.

Once the script has completed, you can check the results in the directory specified in the Upload results step of your GitHub Actions workflow.




Does this setup require a Dockerfile?

Whether or not you need a Dockerfile will depend on the specifics of your inventory script.

If your inventory script can be run natively on the target device, then you don’t need a Dockerfile. In this case, you can simply run the script directly as described in my previous answer.

However, if your inventory script requires a specific runtime environment or dependencies that may not be present on the target device, then you may want to package your script and its dependencies into a Docker image. In this case, you would need to create a Dockerfile that specifies the base image, any additional software to be installed, and the command to run the script.

Here is an example Dockerfile that creates an image containing a Python script and its dependencies:

[bash]
# Use an official Python runtime as the base image
FROM python:3.8-slim
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install the required packages
RUN pip install —no-cache-dir -r requirements.txt
# Define the command to run the script
CMD [“python”, “inventory-script.py”]


In this example, the Dockerfile uses the python:3.8-slim image as the base, sets the working directory to /app, copies the contents of the current directory into the container, installs the required packages using pip, and defines the command to run the script as python inventory-script.py.

After creating the Dockerfile, you can build the Docker image by running the following command:

[ruby]
$ docker build -t inventory-image .

This will build an image named inventory-image based on the contents of the current directory. You can then use this image in your GitHub Actions workflow by replacing image-with-inventory-script with inventory-image in the Run inventory script step