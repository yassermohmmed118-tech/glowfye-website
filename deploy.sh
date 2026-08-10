#!/bin/bash
echo "🚀 Glowfye Deploy Script"
echo "1. Vercel: vercel --prod"
echo "2. Shopify: zip -r shopify.zip shopify-theme/* and upload"
echo "3. GitHub Pages: git push origin main and enable Pages"
echo ""
echo "To deploy to Vercel with token:"
echo "export VERCEL_TOKEN=your_token && npx vercel --prod --yes --token \$VERCEL_TOKEN"
