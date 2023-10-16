def movie_organizer(*args):
  my_dict = {}

  for item in args:
    name = item[0]
    genre = item[1]
    if genre  not in my_dict:
      my_dict[genre] = []
    my_dict[genre].append(name)

  sorted_dict = sorted(my_dict.items(), key = lambda x: (-len(x[1]), x[0]))
  final_result = ''

  for key, value in sorted_dict:
    value = sorted(value)
    final_result += f"{key} - {len(value)}"  +'\n'
    final_result += '\n'.join([f"* {movie}" for movie in value])
    final_result += '\n'

  return final_result
