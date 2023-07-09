from bs4 import BeautifulSoup

html = '''
<a href="/products/40g-liofilizuoti-bananai" class="ProductItem__ImageWrapper "><div class="AspectRatio AspectRatio--short" style="max-width: 2048px;  --aspect-ratio: 1.0"><img class="ProductItem__Image Image--fadeIn lazyautosizes Image--lazyLoaded" data-widths="[200,400,600,700,800,900,1000,1200]" data-sizes="auto" alt="šaltyje džiovinti (liofilizuoti) bananai" data-media-id="22900426834023" data-srcset="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_200x.webp?v=1672949162 200w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_400x.webp?v=1672949162 400w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_600x.webp?v=1672949162 600w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_700x.webp?v=1672949162 700w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_800x.webp?v=1672949162 800w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_900x.webp?v=1672949162 900w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1000x.webp?v=1672949162 1000w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1200x.webp?v=1672949162 1200w" sizes="298px" srcset="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_200x.webp?v=1672949162 200w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_400x.webp?v=1672949162 400w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_600x.webp?v=1672949162 600w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_700x.webp?v=1672949162 700w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_800x.webp?v=1672949162 800w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_900x.webp?v=1672949162 900w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1000x.webp?v=1672949162 1000w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1200x.webp?v=1672949162 1200w">
        <span class="Image__Loader"></span>

        <noscript>
          <img class="ProductItem__Image ProductItem__Image--alternate" src="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-3_600x.webp?v=1672949162" alt="šaltyje džiovinti (liofilizuoti) bananai">
          <img class="ProductItem__Image" src="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_600x.webp?v=1672949162" alt="šaltyje džiovinti (liofilizuoti) bananai">
        </noscript>
      </div>
    </a>

<div class="AspectRatio AspectRatio--short" style="max-width: 2048px;  --aspect-ratio: 1.0"><img class="ProductItem__Image Image--fadeIn lazyautosizes Image--lazyLoaded" data-widths="[200,400,600,700,800,900,1000,1200]" data-sizes="auto" alt="šaltyje džiovinti (liofilizuoti) bananai" data-media-id="22900426834023" data-srcset="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_200x.webp?v=1672949162 200w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_400x.webp?v=1672949162 400w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_600x.webp?v=1672949162 600w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_700x.webp?v=1672949162 700w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_800x.webp?v=1672949162 800w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_900x.webp?v=1672949162 900w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1000x.webp?v=1672949162 1000w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1200x.webp?v=1672949162 1200w" sizes="298px" srcset="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_200x.webp?v=1672949162 200w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_400x.webp?v=1672949162 400w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_600x.webp?v=1672949162 600w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_700x.webp?v=1672949162 700w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_800x.webp?v=1672949162 800w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_900x.webp?v=1672949162 900w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1000x.webp?v=1672949162 1000w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1200x.webp?v=1672949162 1200w">
        <span class="Image__Loader"></span>

        <noscript>
          <img class="ProductItem__Image ProductItem__Image--alternate" src="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-3_600x.webp?v=1672949162" alt="šaltyje džiovinti (liofilizuoti) bananai">
          <img class="ProductItem__Image" src="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_600x.webp?v=1672949162" alt="šaltyje džiovinti (liofilizuoti) bananai">
        </noscript>
      </div>
<img class="ProductItem__Image Image--fadeIn lazyautosizes Image--lazyLoaded" data-widths="[200,400,600,700,800,900,1000,1200]" data-sizes="auto" alt="šaltyje džiovinti (liofilizuoti) bananai" data-media-id="22900426834023" data-srcset="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_200x.webp?v=1672949162 200w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_400x.webp?v=1672949162 400w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_600x.webp?v=1672949162 600w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_700x.webp?v=1672949162 700w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_800x.webp?v=1672949162 800w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_900x.webp?v=1672949162 900w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1000x.webp?v=1672949162 1000w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1200x.webp?v=1672949162 1200w" sizes="298px" srcset="//www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_200x.webp?v=1672949162 200w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_400x.webp?v=1672949162 400w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_600x.webp?v=1672949162 600w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_700x.webp?v=1672949162 700w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_800x.webp?v=1672949162 800w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_900x.webp?v=1672949162 900w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1000x.webp?v=1672949162 1000w, //www.trusthemp.eu/cdn/shop/products/Saltyje-dziovintos-bananai-2_1200x.webp?v=1672949162 1200w">

<div class="ProductItem__Info ProductItem__Info--center"><h2 class="ProductItem__Title Heading">
          <a href="/products/40g-liofilizuoti-bananai">(40g) Liofilizuoti bananai</a>
        </h2><!--BEGIN_AM_REVIEWS:production:PRODUCT_COLLECTION_STAR_WIDGET--><div class="automizely_reviews_product_collection_star_widget" data-product-id="6739269943399" data-ratings="0" data-raters="0" style="display: block; border: none;"> </div><!--END_AM_REVIEWS:production:PRODUCT_COLLECTION_STAR_WIDGET--><div class="ProductItem__PriceList  Heading"><span class="ProductItem__Price Price Text--subdued">€3,40</span></div></div>


<div class="ProductItem__PriceList  Heading"><span class="ProductItem__Price Price Text--subdued">€3,40</span></div>
'''

soup = BeautifulSoup(html, 'html.parser')

# Extract product name and link
product_link_element = soup.select_one('.ProductItem__Title a')
product_name = product_link_element.get_text()
product_link = product_link_element['href']

# Extract product price
product_price_element = soup.select_one('.ProductItem__Price')
product_price = product_price_element.get_text()

# Extract product ID
product_id = soup.select_one('.ProductItem__Title a')['href'].split('/')[-1]

# Extract product weight
product_weight_element = soup.select_one('.ProductItem__Info .ProductItem__Title').next_sibling.strip()
product_weight = product_weight_element.strip("()")

# Print the extracted information
print("Product Name:", product_name)
print("Link:", product_link)
print("Price:", product_price)
print("Product ID:", product_id)
print("Weight:", product_weight)
