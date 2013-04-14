
import bottle

# this is the handler for the default path of the web server

@bottle.route('/')
def home_page():
  mythings = [ 'apple', 'orange', 'banana', 'peach' ]
  # return bottle.template('hello_world', username='Michael', things=mythings)
  return bottle.template('hello_world', { 'username' :'Michael', 'things' : mythings} )

@bottle.post('/favorite_fruit')
def favorite_fruit():
  fruit = bottle.request.forms.get("fruit")
  if (fruit == None or fruit == ""):
    fruit = "No Fruit Selected"

  return bottle.template("fruit_selection.tpl", {'fruit':fruit})

bottle.debug(True)
bottle.run(host='localhost', port=8080)

