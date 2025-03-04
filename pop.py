import os
import django

# Defina o módulo de configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # Ajuste para o nome correto do seu projeto

# Inicializa o Django
django.setup()

import random
from core.trainy.models import Muscles, Exercicies

# Lista de músculos
muscle_names = [
    "Peitoral", "Dorsal", "Bíceps", "Tríceps", "Ombros", "Quadríceps", "Isquiotibiais",
    "Panturrilha", "Glúteos", "Abdômen", "Antebraço", "Trapézio", "Lombar", "Adutores",
    "Abdutores", "Serrátil", "Flexores do punho", "Extensores do punho", "Paravertebrais", "Oblíquos"
]

# Criando os músculos
muscles = [Muscles(name=name, description=f"Músculo {name} usado em vários exercícios.") for name in muscle_names]
Muscles.objects.bulk_create(muscles)

# Buscar os músculos do banco
muscles = list(Muscles.objects.all())

# Lista de exercícios
exercise_names = [
    "Supino Reto", "Supino Inclinado", "Crucifixo", "Pulldown", "Remada Curvada",
    "Rosca Direta", "Rosca Martelo", "Tríceps Testa", "Desenvolvimento", "Elevação Lateral",
    "Agachamento Livre", "Leg Press", "Stiff", "Mesa Flexora", "Panturrilha Sentado",
    "Panturrilha em Pé", "Abdominal Infra", "Prancha", "Rosca Punho", "Extensão de Punho"
]

# Criando os exercícios e associando músculos aleatoriamente
exercises = []
for name in exercise_names:
    exercise = Exercicies(name=name, description=f"Exercício {name} para fortalecimento muscular.")
    exercise.save()  # Precisa salvar antes de adicionar ManyToMany
    exercise.muscle.set(random.sample(muscles, random.randint(1, 3)))  # Associa de 1 a 3 músculos aleatórios
    exercises.append(exercise)

print("🏋️‍♂️ Músculos e exercícios populados com sucesso!")
