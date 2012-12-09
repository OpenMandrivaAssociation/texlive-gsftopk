# revision 26689
# category TLCore
# catalog-ctan /fonts/utilities/gsftopk
# catalog-date 2009-11-09 22:36:07 +0100
# catalog-license gpl
# catalog-version 1.19.2
Name:		texlive-gsftopk
Version:	1.19.2
Release:	3
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
%{_texmfdir}/dvips/gsftopk/render.ps
%doc %{_mandir}/man1/gsftopk.1*
%doc %{_texmfdir}/doc/man/man1/gsftopk.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.19.2-3
+ Revision: 812288
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.19.2-2
+ Revision: 752451
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.19.2-1
+ Revision: 718589
- texlive-gsftopk
- texlive-gsftopk
- texlive-gsftopk
- texlive-gsftopk

