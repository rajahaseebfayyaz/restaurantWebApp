# Testing

During the code development of each function, tests were in place to be sure that it was running as expected. The following sections describe all tests and error handling in place.

## Code Validation Testing

## Automated tests

### **Dango_restaurant_web_app** 

One function from Dango_restaurant_web_app views were tested using unit tests. Manual testing were conducted on all others to ensure no issues on platform. 

<p><img src="./docs/post_unitest_testoverall.jpg"></p>

========================================================================================

### **Members App** 

All functions on the members' app were tested using unit tests. 

  * Views 
<p><img src="./docs/members_unitest_testviews.jpg"></p>

  * Forms 
<p><img src="./docs/members_unitest_testforms.jpg"></p>

  * Members Unittests Overall
<p><img src="./docs/members_unitest_membersoverall.jpg"></p>

<details>
<summary>
Tests covering User Story:

+  "BEST-20 As a user I want to create my user profile"
</summary>

| test_forms| test_views |  
|    ---    |  ---       |
| CreateSignUpFormTest() |  TestRegister() |  
|CreateSignUpFormTestInvalid()|TestLogin()|
||TestLogout()|   | 

</details>
========================================================================================

### **Post App** 

  * Views 
<p><img src="./docs/post_unitest_testviews.jpg"></p>

  * Forms 
<p><img src="./docs/post_unitest_testforms.jpg"></p>

 * Urls 
<p><img src="./docs/post_unitest_testurls.jpg"></p>

 * Models

<p><img src="./docs/post_unitest_testmodels.jpg"></p>

  * Post Unittests Overall
<p><img src="./docs/post_unitest_testoverall.jpg"></p>

<details>
<summary> Tests covering User Stories: 

+ "BEST-2 As a user I want to add a review of my restaurant"
+ "BEST-3 - As a user I want to add a picture on my restaurant review"
+ "BEST-46 - As a user I want to add a rating to my restaurant"
</summary>

| test_models| test_views |  test_forms
|    ---    |  ---       | ---
| BeerReviewTestCase() | AddReviewViewTest()  |  CreateBeerFormTest()
| BeerTestCase()           |BeerRatingView()|
|            |ReviewDetailViewTests()|
|            |PostUpdateViewTests()|
|            |SuccessfulPostUpdateViewTests()|
</details>

<details>
<summary>Tests covering User Story:

+ "BEST-45 -As a user I want to add a restaurant style "
</summary>

| test_forms| test_models |  test_forms |
|    ---    |  ---       |    ----- |
| BeerStyleCreateView() |  BeerStyleTestCase() |  CreateBeerStyleFormTest()|

</details>

<details>
<summary>Tests covering User Story

+ "BEST-57 - As user I want to search my Beer by Style "</summary>

| test_views |   
|  ---       |    
| TestStyleCategoryView() |  

</details>

<details><summary>
Tests covering User Story - "BEST- 52 Search by Beer name"</summary>

| test_views |   
|  ---       |    
| TestStyleCategoryView() |  

</details>

### **Overal Test on plataform** 

At the end of the development of this project (phase 1 - before submission day), used coverage tools to assert that automated tests covered all functions. 

<p><img src="./docs/coverage_beer_app.jpg"></p>

+ **django_beerapp/views.py**

    Uncovered lines on django_beeraap/views are related to pages error handling (400, 403,404 and 500 errors) for the entire platform. These functions were tested manually and no errors have been found. 

+ **post/views.py**

    The lines uncovered by unit tests on post/views.py refers to the update and delete views functions and are described in the bugs section in the readme.md. As this automated test was not done, manual tests were conducted to ensure that features were working as expected and without errors. 

+ **django_beerapp/settings.py**

    These uncovered lines refer to databased used (if production or development), and it was tested manually as well. 

## Integration Test Case

+ On this project, the Incremental Testing method was used.

 Integrated units were checked after the developer finished writing code for every new feature. This approach was used to find defects early and because it was easy to find the cause of the defect thanks to a step-by-step examination. 

+ The integration tests were divided by features/pages and its described below: 

### **Navbar**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click Beer Reviews' navbar button| To be directed to the Beer Reviews Page|
| 2 | Click login's navbar button | To be directed to the Login Page|
| 3 | Click Beer Styles' navbar dropdown button| To be presented with a list of castrated restaurant styles on platform|
| 4 | Click in one of Beer Styles' options on the dropdown menu| To be directed to the restaurant style category page with a piece of information about my search|
| 5 | Add a restaurant name (present on DB) on left field and click search | To be directed to the restaurant category page with a piece of information about my search|
| 5 | Add a restaurant name (not present on DB) on left field and click search | To be directed to the restaurant category page with information about the unexistence of records about this restaurant|
| 6 | A logged User click logout's navbar button | To be logged out and directed to the Home Page|

### **Footer** 

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click on the LinkedIn button| To be directed to the developer's LinkedIn page. |
| 2 | Click on the Github button | To be directed to the developer's GitHub page.|

### **Login**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Enter login credentials and click on the Login button| To be directed to the home page|
| 2 | Enter invalid login credentials and click on the Login button| To be presented to an error message for each invalid field|

### **Register**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Enter all register data and click on the Sign In button| To be directed to the home page, presented to a success message and already logged in|
| 2 | Enter invalid register data in any field and click on the Login button| To be given to an error message|

### **Reviews Card**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click in a restaurant review card| To be directed to the restaurant detail view 
| 2 | Click on Edit button present on card| To be direct to update review page|
| 3 | Click on Delete button present on card| To be direct to confirm deletion page|

### **Buttons**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click Next pagination button| To be direct to the next review page|
| 2 | Click Last pagination button| To be direct to the last review page|
| 3 | Click First pagination button| To be direct to the first review page|
| 4 | Click Previous pagination button| To be direct to the previous review page|
| 5 | Click Go Back button on update review page| To be direct to the previous navigated page|
| 5 | Click Back to Reviews button on detail review page| To be direct to the restaurant reviews navigated page|
| 6 | Click Update button on update review page| To be direct to the restaurant detail navigated page and be presented with new updated review|
| 7 | Click on a star in rating restaurant or update restaurant page | Populate restaurant rating field on review form|
| 8 | Click on restaurant style dropdown button on add restaurant rate or update restaurant page | Be presented with all castrated restaurant styles on DB|
| 9 | Click on restaurant dropdown button on add restaurant rate or update restaurant page | Be presented with all castrated beers on DB|
| 10 | Click on bitterness dropdown button on add restaurant rate or update restaurant page | Be presented with all bitterness choices (1-5)|
| 11 | Click on the money-value dropdown button on add restaurant rate or update restaurant page | Be presented with all money-value choices (1-5)|
| 12 | Click on browse image button on add restaurant rate or update restaurant page | Open your directory to find an image to upload|
| 13 | Check clear on update restaurant page | Clear image previously uploaded to restaurant review|
| 14 | Click Review Your Beer Now on restaurant or restaurant style categories page| To be direct to the add restaurant review page|
| 15 | Click Login and Review on restaurant or restaurant style categories page| To be direct to the login page|

## Python (PEP8) Validation

###  **Django_restaurant App** 

<p float="left">
        <img src="./docs/django_beerapp_urls.png" width="400" height="200" alt="Pep8 validation django_beerapp urls.py"/>
        <img src="./docs/django_beerapp_views.png" width="400" height="200" alt="Pep8 validation django_beerapp views.py"/>
        <img src="./docs/django_beerapp_asgi.png" width="400" height="200" alt="Pep8 validation django_beerapp asgi.py"/>
        <img src="./docs/django_beerapp_wsgi.png" width="400" height="200" alt="Pep8 validation django_beerapp wsgi.py"/>
        <img src="./docs/django_beerapp_settings.png" width="400" height="200" alt="Pep8 validation django_beerapp settings.py"/>
</p>

+ The four too long line errors found on settings were related to links from Cloudinary and Auth Password Validators.

###  **Members App** 

<p float="left">
        <img src="./docs/members-apps.png" width="400" height="200" alt="Pep8 validation members apps.py"/>
        <img src="./docs/members-form.png" width="400" height="200" alt="Pep8 validation members forms.py"/>
        <img src="./docs/members-test_forms.png" width="400" height="200" alt="Pep8 validation members test_forms.py"/>
        <img src="./docs/members-test_views.png" width="400" height="200" alt="Pep8 validation members test_views.py"/>
        <img src="./docs/members-views.png" width="400" height="200" alt="Pep8 validation members views.py"/>
        <img src="./docs/members-urls.png" width="400" height="200" alt="Pep8 validation members urls.py"/>
</p>

### **Post App** 

<p float="left">
        <img src="./docs/post-admin.png" width="400" height="200" alt="Pep8 validation post admin.py"/>
        <img src="./docs/post-apps.png" width="400" height="200" alt="Pep8 validation post apps.py"/>
        <img src="./docs/post-forms.png" width="400" height="200" alt="Pep8 validation post forms.py"/>
        <img src="./docs/post-models.png" width="400" height="200" alt="Pep8 validation post models.py"/>
        <img src="./docs/post-test_models.png" width="400" height="200" alt="Pep8 validation post test_models.py"/>
        <img src="./docs/post-test_urls.png" width="400" height="200" alt="Pep8 validation post test_urls.py"/>
        <img src="./docs/post-test_views.png" width="400" height="200" alt="Pep8 validation post test_views.py"/>
        <img src="./docs/post-urls.png" width="400" height="200" alt="Pep8 validation post urls.py"/>
        <img src="./docs/post-views.png" width="400" height="200" alt="Pep8 validation post views.py"/>
</p>

+ Models error on line 71 is related to Cloudinary defauld image link. 

## HTML Code Validation

All Html pages were validated using W3 tool. 

All results can be foound here

<img src="./docs/validation_home.png" width="400" height="200" alt="Pep8 validation post admin.py"/>
<img src="./docs/validation_register.png" width="400" height="200" alt="Pep8 validation post apps.py"/>
<img src="./docs/validation_login.png" width="400" height="200" alt="Pep8 validation post forms.py"/>
<img src="./docs/validation_stylesearch.png" width="400" height="200" alt="Pep8 validation post models.py"/>
<img src="./docs/validation_stylesearchnoreview.png" width="400" height="200" alt="Pep8 validation post test_models.py"/>
<img src="./docs/validation_beerseach.png" width="400" height="200" alt="Pep8 validation post test_urls.py"/>
<img src="./docs/validation_beerseachnoreview.png" width="400" height="200" alt="Pep8 validation post test_views.py"/>
<img src="./docs/validation403page.png" width="400" height="200" alt="Pep8 validation post urls.py"/>
<img src="./docs/validation404page.png" width="400" height="200" alt="Pep8 validation post views.py"/>
<img src="./docs/validation500page.png" width="400" height="200" alt="Pep8 validation post views.py"/>
<img src="./docs/validation400page.png" width="400" height="200" alt="Pep8 validation post views.py"/>

+ While validating Add revieiw page some warnings and one error could be found :

  1. **Warning:** Possible misuse of aria-label. 
    This warning can be found in 2 occurences in the code. These are added by Django under the hood (not present in original code). The aria label should be present in all fields by design to ensure that accessibility could be reach at maximum level.

  2. **Error:** Duplicate ID id_beer_style. 
    On this case the same Django issue is happening. The id_beer_style is added by django forms when using "{{ style_form.as_p }}" and is not present in the original code. On this way, this error is a known bug and will be added to this section as well.  

<img src="./docs/validatios_add_reviewpage.png" width="400" height="200" alt="Pep8 validation post views.py"/>


## CSS Code Validation

<p float="left">
        <img src="media/readme/css validation/css-validation.png" width="40%" alt="W23C css validation"/>
</p>

## JavaScript Code Validation

### **add_review.js** 

+ On first round of checks, all functions were mmissing semicolon at the end. 
<p>
   <img src= "./docs/add-reviewjs-validation-before.png" width="40%" alt="JShint validation - before"/>
</p>

+ The missing semicolons were placed and all issues have been solved. 
<p>
   <img src= "./docs/add-reviewjs-validation-after.png" width="40%" alt="JShint validation - after "/>
</p>

### **script.js** 
<p>
   <img src= "./docs/scriptjs-validation.png" width="40%" alt="JShint validation - before"/>
</p>

### **toollip.js** 
<p>
   <img src= "./docs/toollipjs-validation.png" width="40%" alt="JShint validation - before"/>
</p>


## Exploratory Testing
========================================================================================

### Initial User Testing (Alpha)

A session was held with an end-user. The feedback obtained is listed below:

1. **Navbar**

   1.1 The page which we are is slightly highlighted. I would like a more visual appealing colour to differentiate better which page I am on.

   1.2 "Beer Styles" dropdown menu is mixed with operational menu options. I would like to have on Left: "Best Beer" (as home), "Beer Reviews", "Beer Styles" and "Search your restaurant". On Right, "Register", "Login", "Logout".

2. **Home Page**

   2.1 I would like to have the option to log in directly from there, without needing to go to the login page and then log in.

3. **Register User Page**

   3.1 When entering a password that did not match, a rapid message appeared on top, but it was impossible to read in time. I would like this message to stick to the bottom of the "Register" container so users can read and understand the error.

   3.2 When logged successfully, I have been redirected to the home page, where I just came. I would like to be redirected to the reviews page to use the information on the website.

4. **Beer Reviews page**

   4.1 I would like to have the option to search, filter and choose different sort options (like Money-Value) directly on-page, without needing to go through the top bar

   4.2 - The "Beer reviews" title looks blended with the background image. I would like to use a larger box with different text sizes or even some logo images. These "Beer reviews" there may also not be required if the top bar uses a more distinct colour when the page is selected.

   4.3 Buttons "First Next Last" looks too close to the card box and background colour blend. I would like a better visual to differentiate between buttons and not random text on the foot of the page.

   4.4 The page should inform default sort order, like displaying "Latest restaurant reviews" instead of just "Beer reviews" and sort that page by review date.

5. **Review Detail Page**

   5.1 at the bottom of the review container, where we see "Written by:", I would rather have it as "Review by: <name of author>"  and on the same row "Created at <date>."


### **Response to the user experience test:**

+ All user feedback was incorporated on the platform except by points 2.1 and 4.1 that is planned to be implemented as future features. 

### Final User Testing (Beta)

On this test, a checklist was developed to guide the user along with all pages and features on the platform. This checklist and the results can be viewed here: 

[Features](media/readme/usertest/userbeta_test1.pdf) <br>
[Pages](media/readme/usertest/userbeta_test2.pdf)

### **Response to the user experience test:**

+ All bugs were fixed before submission.