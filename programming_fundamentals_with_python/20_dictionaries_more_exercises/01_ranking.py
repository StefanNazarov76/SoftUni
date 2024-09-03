contests = {}
submissions = {}

contest = input()
while contest != 'end of contests':
    contest_name, password = contest.split(':')
    contests[contest_name] = password

    contest = input()

submission = input()
while submission != 'end of submissions':
    contest_name, password, username, points = [int(x) if x.isdigit() else x for x in submission.split('=>')]

    if contest_name not in contests or contests[contest_name] != password:
        submission = input()
        continue

    submissions[username] = submissions.get(username, {})
    submissions[username][contest_name] = submissions[username].get(contest_name, 0)
    submissions[username][contest_name] = max(submissions[username][contest_name], points)

    submission = input()

best_user, total_points = '', 0
for user, contest_points in submissions.items():
    current_points = sum(contest_points.values())
    if current_points > total_points:
        total_points = current_points
        best_user = user

print(f'Best candidate is {best_user} with total {total_points} points.')
print('Ranking:')
for user in sorted(submissions):
    print(user)
    for contest_name, points in sorted(submissions[user].items(), key=lambda point: (-point[1])):
        print(f'#  {contest_name} -> {points}')
