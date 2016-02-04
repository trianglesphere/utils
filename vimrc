" Copyright (c) 2015 Joshua Gutow under the MIT License

" Sets how many lines of history VIM has to remember
set history=700

" Stops Vim from beeping
set noerrorbells visualbell t_vb=
if has('autocmd')
    autocmd GUIEnter * set visualbell t_vb=
endif

"Show current line number
set nu

"Show a ruler
set colorcolumn=81
"Stop vim word word wrapping automatically
set tw=0

" Enable syntax highlighting
syntax enable

" Set monokai as the colorscheme
set background=dark
colorscheme solarized

" Set the font to Inconsolata
set guifont=Inconsolata

" 1 tab is 4 columns wide and uses \t
set shiftwidth=4
set tabstop=4
set softtabstop=4
set noexpandtab

" Automatically match the indent of the previous line
set autoindent

" Set fdm to syntax
set fdm=syntax
" Open all folds
set foldlevel=99

" Setting for list view
set lcs=tab:\|\ 

" Use spaces in python and scheme files instead of tabs
autocmd BufRead *.py set expandtab 
autocmd BufRead *.scm set expandtab

