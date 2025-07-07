Overview
========

I created this repo using the Astronomer Quick Airflow Setup for local testing of Airflow Dags and other projects. Below is the quick tips and other info for Astro CLI.

I will reorganize the project structure later, but for n0w this is great to get started.

Project Contents
================

Your Astro project contains the following files and folders:
- notebooks - This folder is used to push the notebooks that are used for the pipeline development.
- dags: This folder contains the Python files for your Airflow DAGs. 
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Airflow Local
===========================

Start Airflow on your local machine by running 'astro dev start'.

This command will spin up five Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- DAG Processor: The Airflow component responsible for parsing DAGs
- API Server: The Airflow component responsible for serving the Airflow UI and API
- Triggerer: The Airflow component responsible for triggering deferred tasks

When all five containers are ready the command will open the browser to the Airflow UI at http://localhost:8080/. You should also be able to access your Postgres Database at 'localhost:5432/postgres' with username 'postgres' and password 'postgres'.

### Important Git / CLI / Astro Commands
=============================================

- astro dev init                                         ( for the first time, initialize the codes)
- astro dev start                                        (spin up the containers and starts local airflow)
- astro dev stop                                         (stops thecontainers from running)
- astro dev kill                                         (kills the instance, will lose all the data unless persisted externally)


==============================================================
- git init                                                 ( for initialiing a local branch)
- git add <files> or git add . (for all changes)           ( this will add the files      )
- git status                                               ( this will check the status of addition of files before commit)
- git commit -m "Commmit Message"                          ( creates the commit with the message)
- git remote add origin <remote-repo-url>                  (this will add remote repo to push/ pull the code changes)
- git push origin <branch>                                 (this will push the code into remote repo)
- git pull --rebase                                        (this will pull the code from the remote repo and merges with the local repo)

==================================================================
- cd                                    (change directory)
- mkdir                                 (create/ make a new directory)
- ls                                    (lists the files)
- rm                                    (remove / delete the files)
- rmdir                                 (remove an entire directory)
- cp                                    (copy the file)
- mv                                    (move the file)
- wget  or curl                         (download from URL)

====================================================================
- hdfs dfs -ls                          (lists the files in the path from Hadoop)
- !gsutil ls                            (lists the files from GCS bucket)



