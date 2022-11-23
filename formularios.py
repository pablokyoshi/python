#formularios.py
#pip install wtforms
#pip install flask_wtf
#pip install wtforms[email]
#pip install wtforms-recaptcha

#Usando google reCAPTCHA v2 para registrar um formulário em Flask,
#para certificar que nao é robo
#para integrar o google recaptcha em um app Flask, nós precisamos
#registrar um site e obter um par de chames api

#Google fornece 4 tipos de reCAPTCHA:
#RECAPTCHA V3 = VALIDA SOLICITAÇÕES COM PONTUAÇÃO
#reCAPTCHA v2 = valida solicitações com "Eu não sou um robô"
#Invisible reCAPTCHA = nao precisa que clique em uma caixa de seleção
#é chamado quando o usuario clica num botao do site
#recaptcha Android

#Passos:
#1. Fazer login no google
#documentação: https://developers.google.com/recaptcha/docs/display
#registro: google.com/recaptcha/admin/create

#2 Etiqueta: primeiro recaptcha
#   Tipo : reCAPTCHA v2 - não sou um robô
#   Dominios: 127.0.0.1 ou localhost (não são suportados por default)
#   verificar email
#   marcar: Aceitar e Enviar

#3 google vai enviar 2 chaves: chave do site e chave secreta
#   salvar as chaves em app.config

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import validators, ValidationError, StringField, IntegerField, SubmitField, PasswordField, EmailField
from wtforms.validators import Length, DataRequired, email, equal_to, optional, NumberRange, Email, EqualTo


class FormCadastro(FlaskForm):
    nome = StringField('Nome', validators=[validators.DataRequired('Faltou digitar o nome'), validators.Length(min=6,max=60)])
    idade = IntegerField('Idade',validators=[DataRequired('Faltou a idade'), NumberRange(min=18, max=60)])
    email = EmailField('E-mail', validators=[Length(min=6, max=60), Email(message='Entre com um e-mail válido'), DataRequired()])
    senha = PasswordField('Senha',validators=[DataRequired(), EqualTo('confirmacao', message='As senhas devem ser correspondentes')])
    confirmacao= PasswordField('Repita a Senha', validators= [DataRequired(), EqualTo('confirmacao', message='As senhas devem ser correspondentes')])

    recaptcha = RecaptchaField()

    submit = SubmitField('Enviar')