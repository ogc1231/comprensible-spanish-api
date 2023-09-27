# Testing

Return back to the [README.md](README.md) file.

## Manual Testing
### Code Validation Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | Screenshot | Notes |
| --- | --- | --- |
| api/permissions.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/api_permissions.png) | Pass: No Errors |
| api/serializers.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/api_serializers.png) | Pass: No Errors |
| api/settings.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/api_settings.png) | Pass: No Errors |
| api/urls.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/api_urls.png) | Pass: No Errors |
| api.views.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/api_views.png) | Pass: No Errors |
| comments/models.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/comments_model.png) | Pass: No Errors |
| comments/serializers.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/comments_serializers.png) | Pass: No Errors |
| comments/urls.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/comments_urls.png) | Pass: No Errors |
| comments/views.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/comments_views.png) | Pass: No Errors |
| favourites/models.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/favourites_models.png) | Pass: No Errors |
| favourites/serializers.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/favourites_serializers.png) | Pass: No Errors |
| favourites/urls.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/favourites_urls.png) | Pass: No Errors |
| favourites/views.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/favourites_views.png) | Pass: No Errors |
| forms/models.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/form_models.png) | Pass: No Errors |
| forms/serializers.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/forms_serializer.png) | Pass: No Errors |
| forms/urls.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/forms_urls.png) | Pass: No Errors |
| forms/views.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/forms_views.png) | Pass: No Errors |
| profiles/models.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/profiles_models.png) | Pass: No Errors |
| profiles/serializers.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/profiles_serilaizer.png) | Pass: No Errors |
| profiles/urls.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/profiles_urs.png) | Pass: No Errors |
| profiles/views.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/profiles_views.png) | Pass: No Errors |
| resources/models.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/resources_models.png) | Pass: No Errors |
| resources/serializers.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/resources_serilizers.png) | Pass: No Errors |
| resources/urls.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/resources_urls.png) | Pass: No Errors |
| resources/views.py | ![screenshot](https://github.com/ogc1231/comprensible-spanish-api/blob/main/documentation/testing-assets/resources_views.png) | Pass: No Errors |


### URL Testing
All urls were tested (development and deployed) make sure they are all working correctly.

| URL | Development | Deployed |
| --- | --- | --- |
| Root Route | Pass | Pass |
| /profiles | Pass | Pass |
| /profiles/id | Pass | Pass |
| /resources | Pass | Pass |
| /resources/id | Pass | Pass |
| /favourites | Pass | Pass |
| /favourites/id | Pass | Pass |
| /comments | Pass | Pass |
| /comments/id | Pass | Pass |
| /forms| Pass | Pass |

### CRUD Testing
All apps were tested to ensure appropriate CRUD functionality was present in the development version of the API

| APP | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
| Profiles(Create Superuser) | Pass | Pass | Pass | n/a |
| Resources | Pass | Pass | Pass | Pass |
| Favourites | Pass | Pass | n/a | Pass |
| Comments | Pass | Pass | Pass | Pass |
| Forms | Pass | Pass | n/a | n/a |

### Search Testing
Search functionality was tested on Resources, to ensure correct results were returned when searching by the relevant search fields.

| APP | Search by Country | Search by Level | Search by Type | Search by Title |
| --- | --- | --- | --- | --- |
| Resources | Pass | Pass | Pass | Pass |

## Automated Testing

## Bugs
**Fixed Bugs**

As previously mentioned, I did only start "counting" bugs when doing the testing of the front and back end application, hence the development process was finished. Since I did heavy testing during development, I could find potential issues already then. Therefore the list with bugs, found during the finalt testing round, is empty.

| Bug | Status |
| --- | --- |
|  |  |

## Unfixed Bugs

There are no remaining bugs that I am aware of.

---

### GitHub **Issues**
**Open Issues**
There are no remaing open issues

**Closed Issues**

| Issue | Status |
| --- | --- |
| [APP 1: Profiles](https://github.com/ogc1231/comprensible-spanish-api/issues/1) | Closed |
| [APP 2: Resources](https://github.com/ogc1231/comprensible-spanish-api/issues/2) | Closed |
| [APP 3: Favourites](https://github.com/ogc1231/comprensible-spanish-api/issues/3) | Closed |
| [APP 4: Comments](https://github.com/ogc1231/comprensible-spanish-api/issues/4) | Closed |
| [APP 5: Forms](https://github.com/ogc1231/comprensible-spanish-api/issues/5) | Closed |
| [APP 6: Resources CRUD Functionality](https://github.com/ogc1231/comprensible-spanish-api/issues/9) | Closed |
| [APP 7: Comments CRUD Functionality](https://github.com/ogc1231/comprensible-spanish-api/issues/10) | Closed |
| [APP 8: Favourites CRUD Functionality](https://github.com/ogc1231/comprensible-spanish-api/issues/11) | Closed |
| [APP 9: Forms CRUD Functionality](https://github.com/ogc1231/comprensible-spanish-api/issues/13) | Closed |
| [APP 10: Profiles CRUD Functionality](https://github.com/ogc1231/comprensible-spanish-api/issues/14) | Closed |
| [APP 11: Profiles Filters](https://github.com/ogc1231/comprensible-spanish-api/issues/15) | Closed |
| [APP 12: Resources Filters](https://github.com/ogc1231/comprensible-spanish-api/issues/16) | Closed |
| [APP 13: Comments Filters](https://github.com/ogc1231/comprensible-spanish-api/issues/17) | Closed |
| [SETUP & DEPLOYMENT: Initial Project Setup](https://github.com/ogc1231/comprensible-spanish-api/issues/6) | Closed |
| [DOCUMENTATION 1: README](https://github.com/ogc1231/comprensible-spanish-api/issues/7) | Closed |
| [DOCUMENTATION 2: TESTING](https://github.com/ogc1231/comprensible-spanish-api/issues/8) | Closed |
| [SETUP & DEPLOYMENT: Heroku Deployment](https://github.com/ogc1231/comprensible-spanish-api/issues/12) | Closed |

**Milestones**

Milestones were used to break the development down into small managable chunks focusing on the most important elements first.

| Milestone | Status |
| --- | --- |
| [MVP Release](https://github.com/ogc1231/sound-burger/milestone/1) | Closed |
| [Second Iteration](https://github.com/ogc1231/sound-burger/milestone/2) | Closed |
| [Third Iteration](https://github.com/ogc1231/sound-burger/milestone/5) | Closed |
| [Bugs](https://github.com/ogc1231/sound-burger/milestone/6) | Open |
| [Setup & Deployment](https://github.com/ogc1231/sound-burger/milestone/4) | Closed |
| [Documentation & Testing](https://github.com/ogc1231/sound-burger/milestone/3) | Closed |