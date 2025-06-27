# 🎨 SCP Font Converter - Professional Web Font Optimizer

> **Modern web-based font converter** that transforms TTF/OTF fonts to optimized WOFF/WOFF2 formats using industry-standard FontTools.

[![.NET](https://img.shields.io/badge/.NET-9.0-512BD4?style=for-the-badge&logo=dotnet)](https://dotnet.microsoft.com/)
[![Blazor](https://img.shields.io/badge/Blazor-Server-512BD4?style=for-the-badge&logo=blazor)](https://blazor.net/)
[![Python](https://img.shields.io/badge/Python-FontTools-3776AB?style=for-the-badge&logo=python)](https://github.com/fonttools/fonttools)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

## ✨ Features

- **🚀 High Performance**: Built with .NET 9 Blazor Server for fast, server-side processing
- **🛠️ Industry Standard**: Uses Google's FontTools library (same tech used by Adobe, Google Fonts)
- **📦 Advanced Optimization**: Font subsetting, hinting removal, and compression options
- **🎨 Modern UI**: Clean, responsive interface with drag & drop support
- **⚡ Real-time Preview**: Live font preview before download
- **🔒 Privacy First**: All processing happens server-side, no data sent to third parties
- **📱 Mobile Friendly**: Fully responsive design works on all devices

## 🎯 Supported Formats

| Input | Output | Compression |
|-------|--------|-------------|
| TTF   | WOFF   | ~40% smaller |
| OTF   | WOFF2  | ~30% better than WOFF |

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/scopweb/scp-font-converter.git
cd scp-font-converter

# Install Python dependencies (FontTools)
pip install fonttools brotli

# Run application
dotnet run
```

Open browser to `https://localhost:5001`

## 📋 Requirements

- **.NET 9.0+** - Latest .NET runtime
- **Python 3.8+** with FontTools
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

## 🔧 Advanced Features

### Font Processing Options
- **📝 Font Subsetting**: Reduce file size by including only needed characters
- **🗜️ Hinting Removal**: Additional compression for web fonts
- **🔤 Custom Character Sets**: Latin, Extended Latin, or custom selection
- **⚡ Batch Processing**: Convert multiple fonts efficiently

### Technical Features
- **🔐 Secure File Handling**: Temporary file cleanup and validation
- **📊 Conversion Statistics**: File size comparisons and savings
- **🌐 Contact System**: Built-in form with anti-spam protection
- **📱 Responsive Design**: Works perfectly on mobile devices

## 🏗️ Tech Stack

```
Frontend:  Blazor Server Components + Bootstrap 5
Backend:   .NET 9 C# + ASP.NET Core
Processing: Python FontTools + Brotli
Security:  Server-side validation + CSRF protection
```

## 🌟 Why SCP Font Converter?

✅ **100% Free & Open Source** - No licensing fees or limitations  
✅ **Professional Quality** - Same tools used by major font foundries  
✅ **Web Optimized** - Specifically designed for web font optimization  
✅ **Privacy Focused** - All processing happens on your server  
✅ **Production Ready** - Used in real-world projects  

## 📊 Performance Benefits

| Format | Original TTF | WOFF | WOFF2 |
|--------|-------------|------|-------|
| Size   | 100%        | ~60% | ~45%  |
| Loading| Baseline    | 40% faster | 55% faster |
| Browser Support | All | IE9+ | Modern |

## 🔧 Configuration

```json
{
  "FontConverter": {
    "TempPath": "./temp",
    "MaxFileSize": "10MB",
    "AllowedExtensions": [".ttf", ".otf"],
    "OutputFormats": ["woff", "woff2"]
  }
}
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Used By

Perfect for:
- **Web Developers** - Optimize fonts for faster loading
- **UI/UX Designers** - Professional font preparation
- **Font Foundries** - Batch conversion workflows
- **Performance Engineers** - Web optimization projects

---

⭐ **Star this repo** if you find it useful! | 🐛 **Report issues** | 💡 **Suggest features**

*Built with ❤️ using .NET 9 and Blazor Server*
