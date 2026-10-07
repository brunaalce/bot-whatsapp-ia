import os
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = FastAPI()

# Inicializa o cliente da OpenAI com a chave de ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"status": "Servidor rodando com sucesso! 🚀"}

@app.post("/webhook")
async def receber_mensagem(request: Request):
    data = await request.json()
    print("Dados recebidos do WhatsApp:", data)
    
    # Exemplo de como você pode chamar a IA para gerar uma resposta inteligente
    try:
        # Aqui você extrairia o texto enviado pelo usuário no WhatsApp
        # Por enquanto, vamos simular uma pergunta padrão caso os dados venham vazios
        pergunta_usuario = "Olá, pode me ajudar?" 
        
        resposta_ia = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual prestativo e simpático."},
                {"role": "user", "content": pergunta_usuario}
            ]
        )
        
        texto_resposta = resposta_ia.choices[0].message.content
        print("Resposta gerada pela IA:", texto_resposta)
        
        return {"status": "sucesso", "resposta_ia": texto_resposta}
        
    except Exception as e:
        return {"status": "erro", "detalhes": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)