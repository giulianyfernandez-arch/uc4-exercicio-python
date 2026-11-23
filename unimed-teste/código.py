documentos_enviados = 0
while documentos_enviados < 3:
    documentos_enviados = documentos_enviados + 1
    print("Recebi o documento", documentos_enviados)

status = "Em avaliação"
documento_legivel = True
if documento_legivel:
    status = "Assinatura"
else:
    status = "Ajuste"
print("Etapa agora:", status)
