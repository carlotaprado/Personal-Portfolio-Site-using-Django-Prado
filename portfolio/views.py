from django.shortcuts import render

def portfolio_list(request):
    # Assuming you have some data related to your portfolio items
    portfolio_items = [...]  # Your portfolio items data
    image_url = "https://mir-s3-cdn-cf.behance.net/project_modules/fs/82cfa7189617081.5a0d875a68664.jpg"  # Your image URL
    return render(request, 'portfolio/portfolio_list.html', {'portfolio_items': portfolio_items, 'image_url': image_url})
