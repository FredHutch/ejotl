# ejotl
Extend JOb Time Limit - extend a slurm job's time limit

Only the Slurm administrator or root may extend a job's time limit.  This script allows a user to do this, but will put some constraints on the activity (e.g. a time limit may only be extended by 30%, only allow 2 extensions, etc.)

## Use

`ejotl <jobid> <time spec>`

`<jobid>`: job ID of a running or queued job
`<time spec>`: a Slurm time specification indicating the amount of time to add/remove.

### Examples

`ejotl 23457243 +3-12`

Extends job 23457243 by three days, twelve hours

`ejotl 12345 -12:13:00`

Removes twelve hours, thirteen minutes from job 12345

`ejotl 98691 4-0`

Explicitly sets the time limit for job 98691 to four days

## Errors and Messages

> To Be Done

## How it Works

This is installed set-uid root (so full-safeties on, please).  When invoked it will make the following checks before altering a job's time limit:

 1. Valid Job ID and time limit
 2. Invoking user is the job's owner
 3. Check request against policy
 
Job changes are stored in AWS simpledb.  Actions are logged using the job ID as the "item" in simpledb.  The attributes store who, what, when.

