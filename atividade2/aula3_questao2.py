# Parte 2: Extração de domínios

urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = [url[4:-4] for url in urls]  # Remove "www." do início e ".com" do fim

print("\nDomínios extraídos:", dominios)
