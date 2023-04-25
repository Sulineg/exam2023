def top_students(scores, n, min_score):
  top_n = []
  for student, score in scores.items():
    if score >= min_score:
      top_n.append((student, score))
  if len(top_n) < n:
    print(
      f" Existuje pouze {len(top_n)} studentů s vyšším skórem než minimální skóre."
    )
  top_n.sort(reverse=True, key=lambda x: x[1])
  result = top_n[:n]
  for student, score in result:
    print(f"{student} ({score})")
  return result


n = 3
min_score = 60
scores = {
  "Student1": 85,
  "Student2": 90,
  "Student3": 72,
  "Student4": 88,
  "Student5": 76,
  "Student6": 94,
  "Student7": 68,
  "Student8": 90
}

top_students(scores, n, min_score)
