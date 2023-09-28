from django.db import models

class ManterOcupacao(models.Model):
    nome_ocupacao = models.CharField(max_length=100)
    def __str__(self):  
        return self.nome_ocupacao
    

class ManterCidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_cidade
    

class TiposAvaliacoes(models.Model):
    nome_tipo_avaliacao = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_tipo_avaliacao
    

class ManterPessoas(models.Model):
    nome_pessoa = models.CharField(max_length=50)  
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    data_nasc = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cidade_pessoa = models.ForeignKey(ManterCidade, on_delete=models.CASCADE)
    ocupacao_pessoa = models.ForeignKey(ManterOcupacao,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_pessoa
    

class ManterEnsino(models.Model):
    nome_ensino = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    site = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_ensino
    

class ManterAreas(models.Model):
    nome_areas = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_areas
    

class ManterCursos(models.Model):
    nome_curso = models.CharField(max_length=100)
    carga_horaria_total = models.CharField(max_length=100) 
    duracao_meses = models.CharField(max_length=100)
    area_saber_curso = models.ForeignKey(ManterAreas, on_delete=models.CASCADE)
    instituicao_curso = models.ForeignKey(ManterEnsino, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_curso
    

class manterSemestres(models.Model):
    periodo_semestre = models.CharField(max_length=50)
    def __str__(self):
        return self.periodo_semestre
    

class ManterDiciplina(models.Model):
    nome_diciplina = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_diciplina
    

class ManterMatriculas(models.Model):
    instituicao_matricula = models.ForeignKey(ManterEnsino, on_delete=models.CASCADE)
    curso_matricula = models.ForeignKey(ManterCursos, on_delete=models.CASCADE)
    pessoa_matricula = models.ForeignKey(ManterPessoas, on_delete=models.CASCADE) 
    data_inicio_matricula = models.CharField(max_length=20)
    data_previsao_termino_matricula = models.CharField(max_length=20)
    def __str__(self):
        return self.data_inicio_matricula
    

class Avaliacoes(models.Model):
    descrisao = models.CharField(max_length=500)
    curso_avaliacao = models.ForeignKey(ManterCursos, on_delete=models.CASCADE)
    disciplina_Avaliacoes = models.ForeignKey(ManterDiciplina, on_delete=models.CASCADE)
    tipo_Avaliacoes = models.ForeignKey(TiposAvaliacoes, on_delete=models.CASCADE)
    def __str__(self):
        return self.descrisao


class ManterFrequencia(models.Model):
    curso = models.ForeignKey(ManterCursos, on_delete=models.CASCADE)
    disciplina_frequencia = models.ForeignKey(ManterDiciplina, on_delete=models.CASCADE)
    numero_fata_frequencia = models.CharField(max_length=50)
    def __str__(self):
        return self.numero_fata_frequencia
    

class ManterTurmas(models.Model):
    nome_turma = models.CharField(max_length=100)
    periodo_semestre_turma = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_turma
    

class Advertencias(models.Model):
    descrisao_advertencia = models.CharField(max_length=500)
    data_advertencia = models.CharField(max_length=50)
    curso_advertencia = models.ForeignKey(ManterCursos, on_delete=models.CASCADE)
    disciplina_advertencia = models.ForeignKey(ManterDiciplina, on_delete=models.CASCADE)
    pessoa_advertencia = models.ForeignKey(ManterPessoas, on_delete=models.CASCADE)
    def __str__(self):
        return self.descrisao_advertencia
    

class ManterDisciplinaCurso(models.Model):
    nome_disciplina_curso = models.CharField(max_length=100)
    carga_horaria_disciplina_curso = models.CharField(max_length=100) 
    curso_disciplina_curso = models.ForeignKey(ManterCursos, on_delete=models.CASCADE)
    periodo_disciplina_curso = models.ForeignKey(manterSemestres, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_disciplina_curso
    