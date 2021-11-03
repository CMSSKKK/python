students = ["정우람", "박으뜸", "배힘찬", "천영웅", "신석기", "배민규", "전민수", "박건우", "박찬호", "이승엽"]
students.sort()
students.remove("박찬호")
print(students[:3])
students.append("이병규")
students.reverse()
students.sort(reverse=True)
print(students)

students[students.index("정우람")] = "정잘남"
print(students)

