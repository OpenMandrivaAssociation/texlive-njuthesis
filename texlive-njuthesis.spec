Name:		texlive-njuthesis
Version:	64797
Release:	1
Summary:	LaTeX thesis template for Nanjing University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/njuthesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njuthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njuthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njuthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The njuthesis class is intended for typesetting Nanjing
University dissertations with LaTeX, providing support for
bachelor, master, and doctoral theses as well as postdoctoral
reports. Compilation of this class requires either XeLaTeX or
LuaLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/njuthesis
%{_texmfdistdir}/tex/latex/njuthesis
%doc %{_texmfdistdir}/doc/latex/njuthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
