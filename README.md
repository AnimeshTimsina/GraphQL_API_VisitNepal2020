# tourism_nepal

## Backend API for vist_nepal app made with django 2.0.7
This is a backend code of API that presents useful information about places, festivals, hotels, restaurants, pubs and cafes of Nepal made with GraphQL and Django
This API can be freely used for development of webapps or mobile apps regarding Nepal's places and culture.
[API URL](https://tourism-nepal.herokuapp.com)

### Link to the app's github repository: [visit_nepal](https://github.com/bimsina/visit_nepal)


#### Required python packages:
- django 2.0.7
- graphene-django==2.3.0

### Installation:
`pip install django`

`pip install graphene-django`


### Running the server

`python manage.py runserver`

Open [localhost:8000](https://localhot:8000) on the browser to open GraphQL Url for writing queries and obtaining data

### Example of a query to get all the information of all the attractions of Nepal:

`query {
  attractionList{	
	  id
    name
    img	
    latitude	
    longitude		
    district		
    province		
    description 		
  }	
}`


### Relevant queries:
- attraction(id:_any_number_)
- attractionByProvince(id:_any_province_num_)
- attractionList
- festival(id:_any_number_)
- festivalList
- pub(id:_any_number_)
- pubList
- restaurant(id:_any_number_)
- restaurantList
- hotel(id:_any_number_)
- hotelList

#### Attribute lists for all these queries can be found on models.py file of this project

#### Mobile App Developer
[Bimsina](https://github.com/bimsina)
### Link to the app's github repository: [visit_nepal](https://github.com/bimsina/visit_nepal)
