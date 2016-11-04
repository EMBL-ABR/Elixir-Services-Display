# bio.tools widget
Queries ELIXIR's [bio.tools](https://bio.tools/) and filters the results to display Australian bioinformatics tools in an accordion style widget.

A modification of [Elixir-Services-Display](https://github.com/tschaka1904/Elixir-Services-Display) by Maximilian Koch.

### Install instructions
1. Install nginx - `sudo apt-get install nginx`
2. Clone this repo
3. Put all files and folders into `/usr/share/nginx/html`
4. Manually run the `toolsAU.py` python script
5. Reload nginx - `sudo service nginx restart`
6. Should be available at `localhost/toolsAU/toolsAU.html`
7. Set up a cron job to run toolsAU.py twice daily, ensuring the resulting `au_tools.json` file is in the `/usr/share/nginx/html`

### Details
Due to API changes, data is no longer pulled from bio.tools directly when a user accesses ToolsAU, and is instead stored locally.

The python script, toolsAU.py, will query tools.au for:
- `contact` containing `Australia`
- `contactEmail` containing `edu.au`
- `creditsInstitution` containing any Australian capital city

All results from these queries are stored in a json file called `au_tools.json`, which the toolsAU widget uses to generate its display.
A cron job is set to update toolsAU using bio.tools twice per day.

### Bio.tools API
The bio.tools API documentation is at [http://biotools.readthedocs.io/en/latest/](http://biotools.readthedocs.io/en/latest/).
ToolsAU uses the `List Resources` section to query for AU tools. 25 results are returned per request.
