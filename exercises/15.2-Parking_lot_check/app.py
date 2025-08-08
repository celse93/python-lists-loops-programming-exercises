parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(array):
  
  state = {
    "total_slots": 0,
    "available_slots": 0, 
    "occupied_slots": 0
  }

  for x in array:
    for y in x:
      if y == 1:
        state["occupied_slots"] += 1
        state["total_slots"] += 1
      elif y == 2:
        state["available_slots"] += 1
        state["total_slots"] += 1
      else:
        None
  
  return state

print(get_parking_lot(parking_state))
  

            
