class Skill:
    def __init__(self, skill, level):
        self.skill = skill
        self.level = level
    def __repr__(self):
        return '{' + self.skill + " " + str(self.level) + '}'
        

class Contributors:
    def __init__(self, name, n):
        self.name = name
        self.n = n
        self.skill=[]
        
    def __repr__(self):
        return '{' + self.name + " " + str(self.n) + '}'
        
    def add_skill(self, skill, level):
        self.skill.append(Skill(skill, level))
            
    def get_level(self, skill):
        for i in self.skill:
            if i.skill == skill.skill:
                return i.level
        return 0


       
class Projects:
    def __init__(self, name, days_c, score, best_b_day):
        self.name = name
        self.days_c = days_c
        self.score = score
        self.best_b_day = best_b_day
        self.contributors = []
        self.skill = []
    
    def add_contributor(self, name, n):
        self.contributors.append(Contributors(name, n))
    
    def add_skill_to_proj(self, skill, level):
        self.skill.append(Skill(skill, level))
    
    def get_level(self, skill):
        for i in self.skill:
            if i.skill == skill.skill:
                return i.level
        return 0
    
    def __repr__(self):
        return '{' + self.name + ', ' + str(self.days_c) + ', ' + str(self.score) + ', ' + str(self.best_b_day) + '}'

file = open("./input_data/c_collaboration.in.txt", 'r')
input=file.readlines() 
c, p = (input[0])[:-1].split(" ")
c=int(c)
p=int(p)
input=input[1:]
num_skills = 0
contri = []
for i in range(c):
    name, num_skills = (input[0])[:-1].split(" ")
    num_skills=int(num_skills)
    contri.append(Contributors(name, int(num_skills)))
    input = input[1:]
    for j in range(num_skills):
        skill, level = (input[j])[:-1].split(" ")
        contri[i].add_skill(skill, int(level))
    input = input[num_skills:]

proj = []
for i in range(p):
    name, days_c, score, best_b_day,n = (input[0])[:-1].split(" ")
    days_c=int(days_c)
    score=int(score)
    best_b_day=int(best_b_day)
    n = int(n)
    proj.append(Projects(name, days_c, score, best_b_day))
    input = input[1:]
    for j in range(n):
        skill, level = (input[j])[:-1].split(" ")
        proj[i].add_skill_to_proj(skill, int(level))
    input = input[n:]


proj.sort(key=lambda x: x.score // x.best_b_day)
    
def check_mentor(contri,skill,project):
    for contributor in contri:
        if contributor.get_level(skill) >= project.get_level(skill):
            return 1
        return 0

def allotment(contri, proj):
    for project in proj:
        print(project.name)
        for skill in project.skill:
            print(skill.skill)
            for contributor in contri:
                print(contributor.name)
                if contributor in project.contributors:
                    continue
                elif contributor.n == 0:
                    continue 
                elif contributor.get_level(skill) < project.get_level(skill)-1:    
                    continue
                elif contributor.get_level(skill) == project.get_level(skill)-1:    
                    if check_mentor(contri, skill, project)==1 :
                        project.contributors.append(contributor)
                        break
                elif contributor.get_level(skill) >= project.get_level(skill):
                    project.contributors.append(contributor)
                    break
                else:
                    continue
        
allotment(contri,proj)   

count=0

file = open("c.txt", 'w')

for project in proj:
    if len(project.contributors) == len(project.skill):
        count = count+1
count = str(count)   
file.write(count+"\n")
for project in proj:
    if len(project.contributors) == len(project.skill):
        file.write(project.name+"\n")
        for contributor in project.contributors:
            if len(project.contributors) == len(project.skill):
                file.write(contributor.name+" ")
        file.write("\n")