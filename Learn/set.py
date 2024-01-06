lessonSet = {'html', 'php', 'javascript', 'java', 'css', 'python', 'laravel', 'angular', 'flutter', 'vue js', 'sql'}

lessonStudent = ('html', 'php', 'javascript', 'java', 'css', 'python', 'typescript')

finalElements = lessonSet.union(lessonStudent)
print('finalElements: ',  finalElements)

lessonSet.remove('spring Boot')

print('lessonSet :', lessonSet)

lessonSet.add('sprint boot')

print('lessonSet :', lessonSet)

# Supposons que nous voulons gérer les cours auxquels les étudians sont inscrits. 
# Utilisez un tuple pour rprésenter les cours d'un étudiant et un set pour représenter l'ensemble des cours disponibles. 
# Ajoutez, supprimez et effectuez des opéations sur les cours.
