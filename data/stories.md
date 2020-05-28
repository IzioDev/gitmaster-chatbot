## goodbye
* bye
  - utter_bye

## thankyou path
* thankyou
    - utter_noworries

## happy path
* greet
  - utter_greet
* request_repository
    - repository_form
    - form{"repository_name": "repository_form"}
    - form{"repository_name": null}
    - utter_slots_values
* thankyou
    - utter_noworries
    - utter_slots_values

## repository requested path
* request_repository
    - repository_form
    - form{"repository_name": "repository_form"}
    - form{"repository_name": null}
    - utter_slots_values
* thankyou
    - utter_noworries
    - utter_slots_values
    
## Directly drop repo name
* inform_repository
    - repository_form
    - form{"repository_name": "repository_form"}
    - form{"repository_name": null}
    - utter_slots_values