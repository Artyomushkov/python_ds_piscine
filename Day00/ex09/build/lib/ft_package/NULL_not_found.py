def NULL_not_found(object: any) -> int:
  if object != object:
    print(f"Cheese: {object} {type(object)}")
    return 0
  if not object:
    if object is None:
      print(f"Nothing: {object} {type(object)}")
    elif type(object) is int:
      print(f"Zero: {object} {type(object)}")
    elif type(object) is str:
      print(f"Empty: {type(object)}")
    elif type(object) is bool:
      print(f"Fake: {object} {type(object)}")
    return 0
  return 1