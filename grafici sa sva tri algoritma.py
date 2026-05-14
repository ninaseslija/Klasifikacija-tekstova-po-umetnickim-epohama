import matplotlib.pyplot as plt
import numpy as np

# Podaci
models = ['Slučajna šuma', 'Stablo odlučivanja', 'Naivni Bajes']
bow_scores = [0.5706, 0.5231, 0.8595]
tfidf_scores = [0.5674, 0.5248, 0.8624]

x = np.arange(len(models))  # pozicije za grupe stubića
width = 0.35  # širina stubića

# Stilovi i boje
plt.figure(figsize=(8, 5))
plt.bar(x - width/2, bow_scores, width, label='Bag of Words', color='#FFB3C1', edgecolor='black')
plt.bar(x + width/2, tfidf_scores, width, label='TF-IDF', color="#FF6F61", edgecolor='black')

# Oznake i stil
plt.xticks(x, models, fontsize=11)
plt.ylabel('F1 Score', fontsize=12)
plt.title('Rezultati klasifikacije', fontsize=14, fontweight='bold', pad=15)
plt.ylim(0, 1.0)

# ✅ Legenda unutar grafikona, iznad stubića za Slučajnu šumu, sa belim kvadratom
plt.legend(
    loc='upper left',
    bbox_to_anchor=(0.02, 0.98),
    frameon=True,
    facecolor='white',
    edgecolor='black'
)

# Prikaz brojeva iznad stubića
for i in range(len(models)):
    plt.text(x[i] - width/2, bow_scores[i] + 0.015, f'{bow_scores[i]:.3f}', ha='center', fontsize=10)
    plt.text(x[i] + width/2, tfidf_scores[i] + 0.015, f'{tfidf_scores[i]:.3f}', ha='center', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
