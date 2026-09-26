import os, django, sys
def run():
    import os, django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grocery_site.settings')
    django.setup()
    from store.models import Product
    MEDIA = os.path.join(os.path.dirname(__file__), '..', 'media','products')
    MEDIA = os.path.normpath(MEDIA)
    created = 0
    if not os.path.exists(MEDIA):
        print('Media folder not found:', MEDIA)
        return
    for fname in sorted(os.listdir(MEDIA)):
        if fname.lower().endswith(('.png','.jpg','.jpeg','.gif','.webp')):
            name = os.path.splitext(fname)[0].replace('_',' ').title()
            p, ok = Product.objects.get_or_create(name=name)
            p.image = 'products/' + fname
            p.price = 49.00
            p.discount = 0.00
            p.save()
            created += 1
    print('Imported {} products.'.format(created))

if __name__ == '__main__':
    run()
