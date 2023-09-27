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

## Automated Testing