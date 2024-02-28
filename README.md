## Anotações:

## Models
````

class Avaliacao(Base):
    id = models.TextField(primary_key=True, default=str(uuid.uuid4), editable=False)
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']
        ordering = ['id']

````

- Quando queremos relacionar one to one com atributos por exemplo: nesta classe só é permitido uma avaliação, ou seja, um email não pode ser repetir no mesmo curso.
Passamos na Class Meta -> unique_together= ['email', 'curso']