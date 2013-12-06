# revision 29764
# category TLCore
# catalog-ctan /fonts/utilities/gsftopk
# catalog-date 2012-07-13 12:47:32 +0200
# catalog-license gpl
# catalog-version 1.19.2
Name:		texlive-gsftopk
Version:	1.19.2
Release:	7
Summary:	Convert "ghostscript fonts" to PK files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/gsftopk
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gsftopk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gsftopk.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-gsftopk.bin

%description
Designed for use with xdvi and dvips this utility converts
Adobe Type 1 fonts to PK bitmap format. It should not
ordinarily be much used nowadays, since both its target
applications are now capable of dealing with Type 1 fonts,
direct.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/gsftopk/render.ps
%doc %{_mandir}/man1/gsftopk.1*
%doc %{_texmfdistdir}/doc/man/man1/gsftopk.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
