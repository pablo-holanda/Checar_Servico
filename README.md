# Checar_Servico

```python
        class ModeloPadrao(models.Model):
        nome = models.CharField(maxlength=120)
        .
        .
        .
        etc = models.etc
    
        def _unicode(self):
            return '%s' % self.nome
    
        class Meta:
            abstract = True
```
