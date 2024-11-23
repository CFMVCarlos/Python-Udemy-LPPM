morning = {"Java", "C", "Ruby", "Lisp", "C#", "Rust"}
afternoon = {"Python", "C#", "Java", "C", "Ruby"}

#! Symmetric difference is commutative and is used to find the elements that are in one set or the other, but not in both
# possible_languages = morning.symmetric_difference(afternoon)
possible_languages = morning ^ afternoon

print(f"{possible_languages = }")
