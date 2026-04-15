
#  Upload Temporário de Imagens (Cloudinary)

Aplicação web simples para enviar uma imagem e receber um link público que **expira automaticamente após 5 minutos**. Utiliza a API do Cloudinary para armazenamento e exclusão automática.

##  Funcionalidades

- Upload de imagens (PNG, JPEG, GIF, WEBP).
- Geração de URL pública acessível de qualquer lugar.
- Botão para copiar o link com feedback visual.

##  Tecnologias Utilizadas

- **Backend:** Python + Flask
- **Armazenamento:** [Cloudinary API](https://cloudinary.com/)
- **Frontend:** HTML5, CSS3, JavaScript (vanilla)

##  Como Rodar Localmente

### Pré-requisitos

- Python 3.7 ou superior instalado
- Git (para clonar o repositório)
- Uma conta gratuita no [Cloudinary](https://cloudinary.com/) para obter as credenciais de API

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
   *Se você não tiver o arquivo `requirements.txt`, crie-o com o seguinte conteúdo:*
   ```
   Flask
   cloudinary
   ```

4. **Obtenha suas credenciais do Cloudinary:**
   - Acesse [Cloudinary Console](https://console.cloudinary.com/).
   - Faça login ou crie uma conta gratuita.
   - No **Dashboard**, você verá:
     - **Cloud Name** (ex: `dtgshlcqt`)
     - **API Key**
     - **API Secret** (clique no ícone de olho para revelar)

5. **Configure as credenciais no projeto:**
   - Abra o arquivo `app.py` e localize as linhas:
   <img width="600" alt="Credenciais Cloudinary no app.py" src="https://github.com/user-attachments/assets/4f941314-6332-42ef-a58d-d88ef1599e55" />

    - Substitua os valores entre aspas pelas suas credenciais reais.

   > ** Dica de segurança:** Nunca faça commit das chaves reais no GitHub. Para produção, utilize variáveis de ambiente (veja seção *Configuração Segura* abaixo).

7. **Execute a aplicação:**
   ```bash
   python app.py
   ```

8. **Acesse no navegador:**
   - Abra `http://127.0.0.1:5000`


## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.


