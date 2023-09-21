/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: wberger <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/09 11:48:30 by wberger           #+#    #+#             */
/*   Updated: 2022/07/09 12:08:30 by wberger          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */
void	ft_rev_int_tab(int *tab, int size)
{
	int	i;
	int	j;
	int	inv;

	i = 0;
	j = size - 1;
	while (i < (size / 2))
	{
		inv = tab[i];
		tab[i] = tab[j];
		tab[j] = inv;
		i++;
		j--;
	}
}
