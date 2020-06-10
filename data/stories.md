## goodbye
* bye
    - utter_bye
    - action_restart

## thankyou path
* thankyou
    - utter_noworries

## happy path
* greet
    - utter_greet
* request_repository
    - repository_form
    - form{"name": "repository_form"}
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart
    
## happy path no thanks
* greet
    - utter_greet
* request_repository
    - repository_form
    - form{"name": "repository_form"}
    - form{"name": null}

## repository requested path
* request_repository
    - repository_form
    - form{"name": "repository_form"}
    - form{"name": null}
* thankyou
    - utter_noworries
    - action_restart

## Directly drop repo name
* inform_repository
    - repository_form
    - form{"name": "repository_form"}
    - form{"name": null}