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
I have conducted a series of automated tests on my application.

I have tested the "Matches" and the "Guns" app via unit test.
- [Resource Unit Testing](/resources/tests.py)

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive. However, I wanted to include a few example tests for CRUD functionality and permissions.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test`

All testcases are successfully executed:

[screenshot](docs/testing/unit_matches_guns.png)

ResourceListViewTests
```python
class ResourceListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='sam', password='pass')

    def test_can_list_resources(self):
        sam = User.objects.get(username='sam')
        Resource.objects.create(owner=sam, title='How to Spanish')
        response = self.client.get('/resources/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_user_not_logged_in_cant_create_resource(self):
        response = self.client.post('/resources/', {'title': 'How to Spanish'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

ResourceListViewTests
```Python
class ResourceDetailViewTests(APITestCase):
    def setUp(self):
        sam = User.objects.create_user(username='sam', password='pass')
        tam = User.objects.create_user(username='tam', password='pass')
        Resource.objects.create(
            owner=sam, title='How to Spanish',
            desc='sams content',
            resource_url='www.dog.com'
        )
        Resource.objects.create(
            owner=tam, title='Dreaming Spanish',
            desc='tams content',
            resource_url='www.cat.com'
        )

    def test_can_retrieve_resource_using_valid_id(self):
        response = self.client.get('/resources/1/')
        self.assertEqual(response.data['title'], 'How to Spanish')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_resource_using_invalid_id(self):
        response = self.client.get('/resources/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cant_update_another_users_resource(self):
        self.client.login(username='sam', password='pass')
        response = self.client.put(
            '/resources/2/', {'title': 'Charlas Hispanas'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

## Bugs
**Fixed Bugs**
Errors in code "bugs" were fixed on discovery during development.

## Unfixed Bugs

There are no remaining bugs that I am aware of.

### GitHub **Issues**
**Open Issues**
There are no remaing open issues.

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
Milestones were used to group issues.

| Milestone | Status |
| --- | --- |
| [Documentation & Testing](https://github.com/ogc1231/comprensible-spanish-api/milestone/1) | Closed |
| [Setup & Deployment](https://github.com/ogc1231/comprensible-spanish-api/milestone/2) | Closed |
| [APP](https://github.com/ogc1231/comprensible-spanish-api/milestone/3) | Open |
| [Bugs](https://github.com/ogc1231/comprensible-spanish-api/milestone/6) | Closed |