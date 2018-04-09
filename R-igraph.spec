#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-igraph
Version  : 1.2.1
Release  : 3
URL      : https://cran.r-project.org/src/contrib/igraph_1.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/igraph_1.2.1.tar.gz
Summary  : Network Analysis and Visualization
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ LGPL-2.1
Requires: R-igraph-lib
Requires: R-pkgconfig
BuildRequires : R-pkgconfig
BuildRequires : clr-R-helpers
BuildRequires : gmp-dev
BuildRequires : libxml2-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
handle large graphs very well and provides functions for generating random
  and regular graphs, graph visualization, centrality methods and much more.

%package lib
Summary: lib components for the R-igraph package.
Group: Libraries

%description lib
lib components for the R-igraph package.


%prep
%setup -q -c -n igraph

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523310083

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523310083
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library igraph
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library igraph
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library igraph
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library igraph|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/igraph/AUTHORS
/usr/lib64/R/library/igraph/CITATION
/usr/lib64/R/library/igraph/DESCRIPTION
/usr/lib64/R/library/igraph/INDEX
/usr/lib64/R/library/igraph/Meta/Rd.rds
/usr/lib64/R/library/igraph/Meta/demo.rds
/usr/lib64/R/library/igraph/Meta/features.rds
/usr/lib64/R/library/igraph/Meta/hsearch.rds
/usr/lib64/R/library/igraph/Meta/links.rds
/usr/lib64/R/library/igraph/Meta/nsInfo.rds
/usr/lib64/R/library/igraph/Meta/package.rds
/usr/lib64/R/library/igraph/NAMESPACE
/usr/lib64/R/library/igraph/NEWS.md
/usr/lib64/R/library/igraph/R/igraph
/usr/lib64/R/library/igraph/R/igraph.rdb
/usr/lib64/R/library/igraph/R/igraph.rdx
/usr/lib64/R/library/igraph/README.md
/usr/lib64/R/library/igraph/benchmarks/correlated.R
/usr/lib64/R/library/igraph/benchmarks/local.scan.R
/usr/lib64/R/library/igraph/benchmarks/time_call.R
/usr/lib64/R/library/igraph/benchmarks/time_dirSelect.R
/usr/lib64/R/library/igraph/benchmarks/time_fr_layout.R
/usr/lib64/R/library/igraph/benchmarks/time_kk_layout.R
/usr/lib64/R/library/igraph/benchmarks/time_print.R
/usr/lib64/R/library/igraph/benchmarks/time_sgm.R
/usr/lib64/R/library/igraph/benchmarks/time_sir.R
/usr/lib64/R/library/igraph/demo/centrality.R
/usr/lib64/R/library/igraph/demo/cohesive.R
/usr/lib64/R/library/igraph/demo/community.R
/usr/lib64/R/library/igraph/demo/crashR.R
/usr/lib64/R/library/igraph/demo/hrg.R
/usr/lib64/R/library/igraph/demo/smallworld.R
/usr/lib64/R/library/igraph/help/AnIndex
/usr/lib64/R/library/igraph/help/aliases.rds
/usr/lib64/R/library/igraph/help/igraph.rdb
/usr/lib64/R/library/igraph/help/igraph.rdx
/usr/lib64/R/library/igraph/help/paths.rds
/usr/lib64/R/library/igraph/html/00Index.html
/usr/lib64/R/library/igraph/html/R.css
/usr/lib64/R/library/igraph/html_library.license.terms
/usr/lib64/R/library/igraph/html_library.tcl
/usr/lib64/R/library/igraph/igraph.gif
/usr/lib64/R/library/igraph/igraph2.gif
/usr/lib64/R/library/igraph/libs/symbols.rds
/usr/lib64/R/library/igraph/my_html_library.tcl
/usr/lib64/R/library/igraph/tkigraph_help/communities.html
/usr/lib64/R/library/igraph/tkigraph_help/index.html
/usr/lib64/R/library/igraph/tkigraph_help/style.css
/usr/lib64/R/library/igraph/tkigraph_help/tkigraph-main.gif

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/igraph/libs/igraph.so
/usr/lib64/R/library/igraph/libs/igraph.so.avx2
/usr/lib64/R/library/igraph/libs/igraph.so.avx512
